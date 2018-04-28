entries = []

f = open('test.csv')
for line in f:
    line = line.strip()
    if line:
        entries.append(line.split(','))
f.close()

out = open('test.csv', 'w')    # Achtung, löscht den Inhalt der Datei!

for entry in sorted(entries):
    print(','.join(entry), file=out)

out.close()
