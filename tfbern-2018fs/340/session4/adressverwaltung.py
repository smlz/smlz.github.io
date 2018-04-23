
adressen = []

f = open('adressbuch.csv')
for zeile in f:
    vorname, name, email = zeile.strip().split(',')
    print(f'"{vorname} {name}" <{email}>')
    adressen.append([vorname, name, email])
f.close()

adressen.append(['Klara', 'Ito', 'ki@tfbern.ch'])

f = open('adressbuch.csv', 'w') # 'w' überschreibt, 'a' hängt an
for adresse in adressen:
    print(adresse[0], adresse[1], adresse[2], sep=',', file=f)

f.close()
