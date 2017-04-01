person = {
  'vorname': 'Hans',
  'nachname': 'Müller',
}

print(f"{person['vorname']} {person['nachname']}")
print(person['vorname'], person['nachname'])

print('nachname' in person)

#update
person['nachname'] = 'Meier'
person['telefon'] = '063 234 22 12'

print(person)

print(person['telefon'])
try:
    print(person['ort'])
except KeyError:
    print('Kein Ort vorhanden')

print(person.get('plz', '<keine PLZ>'))

for key in person:     # Einfachsten
    print(key, person[key])

for key in person.keys():
    print(key)

for val in person.values():
    print(val)

for key, val in person.items():  # Direkt beide Werte
    print(key, val)
