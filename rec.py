#!/usr/bin/python3
#from __future__ import print_function, division, absolute_import, unicode_literals

import base64
import glob
import json
import os
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

    with tempfile.NamedTemporaryFile() as logfile,  \
         tempfile.NamedTemporaryFile() as timingfile, \
         open(pjoin(wd, session_fname), 'w') as outfile, \
         open(pjoin(wd, index_fname), 'r+', encoding='UTF-8') as indexfile:

        proc = subprocess.Popen(['script', '--flush', '--quiet',
                                 '--command={}'.format(command),
                                 '--timing={}'.format(timingfile.name),
                                 logfile.name],
                                cwd=pjoin(wd, session_dir))
        proc.wait()
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

        indexcontents = indexfile.read()

        session_title = input("Session title: ")
        if not session_title:
            session_title = session_fname.replace('.json', '')\
                                         .replace('_', ' ')\
                                         .capitalize()
        cursor = config.get('index_file_cursor', '<!-- REC-SESSIONS -->')
        if 'index_entry_template' in config:
            link_template = config['index_entry_template']
        else:
            git_root = subprocess.check_output(['git', 'rev-parse',
                                                '--show-toplevel'])
            git_root = str(git_root, encoding='utf-8').strip()
            server_path = '/' + os.path.relpath(wd, start=git_root) + '/'
            link_template = '<a href="/console.html?data=' + server_path \
                            + '{filename}">{title}</a><br/>'

        link = link_template.format(filename=session_fname, title=session_title)
        indexcontents = indexcontents.replace(cursor, link + cursor)
        indexfile.seek(0)
        indexfile.truncate()
        indexfile.write(indexcontents)

    if config.get('commit', False):
        subprocess.call(['git', 'add', pjoin(wd, index_fname),
                         pjoin(wd, session_fname)])
        subprocess.call(['git', 'commit', '-m',
                         'Auto-commit: ' + session_title])
        if config.get('push', False):
            subprocess.call(['git', 'push'])


if __name__ == '__main__':
    main(*sys.argv[1:])
