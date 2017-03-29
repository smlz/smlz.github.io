#!/usr/bin/python3
#from __future__ import print_function, division, absolute_import, unicode_literals

import base64
import collections
import glob
import json
import os
import pyinotify
import subprocess
import sys
import tempfile

pjoin = os.path.join

CONFIG_FILE_NAME = '.rec.json'

def find_config(startdir):
    path = pjoin(startdir, CONFIG_FILE_NAME)
    if os.path.exists(path):
        return path
    elif (startdir == '/'):
        return None
    else:
        return find_config(os.path.dirname(startdir))


def get_session_file_name(working_dir, file_name_prefix):
    prefix = pjoin(working_dir, file_name_prefix)
    extension = '.json'
    existing = glob.glob(prefix + '??' + extension)
    if existing:
        last = sorted(existing)[-1]
        last_num = int(last[len(prefix): -len(extension)])
        fname = '{}{:02d}.json'.format(file_name_prefix, last_num + 1)
    else:
        fname = file_name_prefix + '01.json'
    open(pjoin(working_dir, fname), 'a').close()  # create file to prevent race condition
    return fname


def main(command='bash'):
    config_file = find_config(os.getcwd())
    if config_file:
        wd = os.path.dirname(config_file)
        config = json.load(open(config_file))
    else:
        config = {}
        wd = os.getcwd()

    session_fname = get_session_file_name(wd, config.get('session_file_prefix', 'session_'))
    index_fname = config.get('index_file', 'index.html')

    session_dir = os.path.dirname(session_fname)

    git_root = subprocess.check_output(['git', 'rev-parse',
                                        '--show-toplevel'])
    git_root = str(git_root, encoding='utf-8').strip()
    server_path = '/' + os.path.relpath(wd, start=git_root) + '/'

    with tempfile.NamedTemporaryFile() as logfile,  \
         tempfile.NamedTemporaryFile() as timingfile, \
         open(pjoin(wd, session_fname), 'w') as outfile, \
         open(pjoin(wd, index_fname), 'r+', encoding='UTF-8') as indexfile:

        wm = pyinotify.WatchManager()
        wm.add_watch(pjoin(wd, session_dir), pyinotify.IN_CLOSE_WRITE)

        proc = subprocess.Popen(['script', '--flush', '--quiet',
                                 '--command={}'.format(command),
                                 '--timing={}'.format(timingfile.name),
                                 logfile.name],
                                cwd=pjoin(wd, session_dir))
        proc.wait()

        events = []
        notifier = pyinotify.Notifier(wm, events.append)
        if notifier.check_events(0):
            notifier.read_events()
            notifier.process_events()
        wm.close()
        touched_files = [e.name for e in events
                         if os.path.isfile(pjoin(wd, session_dir, e.name))]
        touched_files = list(collections.OrderedDict.fromkeys(touched_files))

        columns = int(subprocess.check_output(['tput', 'cols']).strip())
        lines = int(subprocess.check_output(['tput', 'lines']).strip())
        data = {
            'script': str(base64.b64encode(b''.join(logfile.readlines()[1:])),
                          encoding='ascii'),
            'timings': [(float(time), int(cnt)) for time, cnt in
                        (line.split() for line in timingfile.readlines())],
            'columns': columns,
            'lines': lines,
        }
        json.dump(data, outfile)

        session_title = input("Session title: ")
        if not session_title:
            session_title = session_fname.replace('.json', '')\
                                         .replace('_', ' ')\
                                         .capitalize()
        added_files = []
        for f in touched_files:
            answer = input("Add file '{}'? [Y/n] ".format(f)).strip().lower()
            if answer == '' or answer[0] == 'y':
                added_files.append(f)

        term_session_cursor = config.get('index_file_cursor',
                                         '<!-- REC-TERM-SESSION -->')
        term_session_templ = config.get('term_session_template',
                                        '<a href="/console.html?data=' \
                                        + server_path \
                                        + '{filename}">{title}</a><br/>')
        files_cursor = config.get('files_cursor',
                                  '<!-- REC-FILES -->')
        files_templ = config.get('files_template',
                                 '<a href="{path}">{filename}</a><br/>')

        data = indexfile.read()

        term_session = term_session_templ.format(filename=session_fname,
                                                 title=session_title)
        data = data.replace(term_session_cursor,
                            term_session + term_session_cursor)
        files = ''.join(files_templ.format(filename=f,
                                           path=pjoin(session_dir, f))
                          for f in added_files)
        data = data.replace(files_cursor, files + files_cursor)
        indexfile.seek(0)
        indexfile.truncate()
        indexfile.write(data)

    if config.get('commit', False):
        subprocess.call(['git', 'add', pjoin(wd, index_fname),
                         pjoin(wd, session_fname)]\
                         + [pjoin(wd, session_dir, f) for f in added_files])
        subprocess.call(['git', 'commit', '-m',
                         'Auto-commit: ' + session_title])
        if config.get('push', False):
            subprocess.call(['git', 'push'])


if __name__ == '__main__':
    main(*sys.argv[1:])
