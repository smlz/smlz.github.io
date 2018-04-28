import os.path
import sys

if len(sys.argv) != 2:
    print(f"Error! Usage python3 {sys.argv[0]} <FILENAME>")
    sys.exit(1)
filename = sys.argv[1]

if not os.path.isfile(filename):
    print(f"Error! File '{filename}' not found")
    sys.exit(2)

entries = []

f = open(filename)
for line in f:
    line = line.strip()
    if line:
        entries.append(line.split(','))
f.close()

out = open(filename, 'w')    # Achtung, löscht den Inhalt der Datei!

for entry in sorted(entries):
    print(','.join(entry), file=out)

out.close()
