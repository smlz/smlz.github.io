def print_2(eins, zwei):
    print(eins, zwei)

def print_1(eins):
    print(eins)

def print_nichts():
    print('Nichts')


print_2('Zwiebelnsauce', 'Bratwurst')
print_1('Eule')
print_nichts()

vorname = 'Marco'
nachname = 'Schmalz'
print_2(vorname, nachname)

# Speziell in Python
print_2(zwei=nachname, eins=vorname)

print(1, 2, 3, sep='-')

# Default-Werte für Argumente oder auch optionale Argumente

def print_etwas_oder_nichts(etwas=''):
    if etwas == '':
        print('Nichts')
    else:
        print(etwas)

print_etwas_oder_nichts('etwas')
print_etwas_oder_nichts()

def multiplizieren(a, b):
    print('MULTIPLIZIEREN', a, b)
    return a * b

def quadrieren(a):
    print('QUADRIEREN', a)
    return a * a

def addieren(a, b):
    print('ADDIEREN', a, b)
    return a + b

a = 3
b = 4
a_quadrat = quadrieren(a)
b_quadrat = quadrieren(b)
c_quadrat = addieren(a_quadrat, b_quadrat)
print(f"{a}² + {b}² = {c_quadrat}")
