f = open('adressbuch.csv')

adressbuch = []

for line in f:
    werte = line.strip().split(';')
    eintrag = {'Name': werte[0], 'Vorname': werte [1]}
    adressbuch.append(eintrag)

f.close()

for eintrag in adressbuch:
    print(eintrag['Vorname'], eintrag['Name'])

f = open('adressbuch.csv', 'w')

def invert(s):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)

for eintrag in adressbuch:
    print(invert(eintrag['Name']), invert(eintrag['Vorname']), file=f, sep=';')

f.close()

