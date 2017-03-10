#!/usr/bin/python3
import csv
import datetime

heute = datetime.date.today()

file = open('../team.csv')
reader = csv.DictReader(file)
entries = list(reader)

lehrlinge = []

for entry in entries:
    if 'Lehre' in entry['Gruppen'].split(', '):
        lehrlinge.append(entry)

for lehrling in lehrlinge:
    datumsliste = lehrling['Geburtstag'].split('.')
    lehrling['Geburtstag'] = '-'.join(reversed(datumsliste))

for lehrling in lehrlinge:
    print(lehrling['Geburtstag'])
juengste = lehrlinge[0]
for lehrling in lehrlinge[1:]:
    if lehrling['Geburtstag'] > juengste['Geburtstag']:
        juengste = lehrling

print(juengste)
