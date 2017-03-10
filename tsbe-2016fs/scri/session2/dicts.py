kantonskuerzel = {
  'Appenzell Ausserrhoden': 'AR',
  'Appenzell Innerrhoden': 'AI',
  'Bern': 'BE',
}

hauptstaedte = {
  'BE': 'Bern',
  'AR': 'Herisau',
  'AI': 'Zapponell',
}

print('Das Kürzel von Ausserrhoden ist', kantonskuerzel['Appenzell Ausserrhoden'])


for name, kuerzel in kantonskuerzel.items():
    print(name, hauptstaedte[kuerzel])
