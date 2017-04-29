#!/usr/bin/python3.6
finanzausgleich = { 'ZH': 22, 'BE': -20, 'ZG': 16, 'VS': -15 }
print(finanzausgleich['BE'])
print(finanzausgleich.get('ZG', 0))
print(finanzausgleich.get('AG', 0))

summe = 0
for kanton, zahl in finanzausgleich.items():
    summe += zahl
if summe != 0:
    print(f"Warnung: Gesamtsumme = {summe}")

kantonsnamen = { 'ZH': 'Zürich', 'BE': 'Bern', 'ZG': 'Zug', 'VS': 'Wallis' }
geberkantone = []
nehmerkantone = []
for kanton, zahl in finanzausgleich.items():
    if zahl < 0:
       nehmerkantone.append(kantonsnamen[kanton])
    else:
       geberkantone.append(kantonsnamen[kanton])

print(f'Geberkantone ({len(geberkantone)}):')
print('\n'.join(geberkantone))
print('-' * 5)
print(f'Nehmerkantone ({len(nehmerkantone)}):')
for kanton in nehmerkantone:
    print(f' * {kanton}')
