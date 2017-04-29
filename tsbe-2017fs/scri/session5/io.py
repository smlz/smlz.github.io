f = open('adressbuch.csv')

adressbuch = []

for line in f:
    liste = line.strip().split(';')
    eintrag = {}
    adressbuch.append(eintrag)

f.close()

#adressbuch = [
#  {'Name': 'Müller', 'Vorname': 'Beatrice'},
#  {'Name': 'Meier', 'Vorname': 'Hans'},
#  {'Name': 'Meier', 'Vorname': 'Peter'},
#]

f = open('adressbuch.csv', 'w')

for eintrag in adressbuch:
    print(eintrag['Name'], eintrag['Vorname'], file=f, sep=';')

f.close()

