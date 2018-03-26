
zahlen = [1, 2, 3, 4, 5, 6]

quadratzahlen = []

for zahl in zahlen:
    quadratzahlen.append(zahl * zahl)


kubikzahlen = [ zahl ** 3 for zahl in zahlen  ]


de_en = {'Hund': 'dog', 'Katze': 'cat'}

for key, val in de_en.items():
    pass

en_de = {val: key  for key, val in de_en.items() }
