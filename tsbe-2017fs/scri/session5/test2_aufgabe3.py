#!/usr/bin/python3.6

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def durchschnitt(a, b):
    return (a + b) / 2

def gleiches_vorzeichen(a, b):
    return (a >= 0 and b >= 0) or (a < 0 and b < 0)

while True:
    a = float(input('Erste Zahl: '))
    b = float(input('Zweite Zahl: '))
    op = input('Operation: ')
    if op == '+':
        resultat = plus(a, b)
        print(f'{a} + {b} = {resultat}')
    elif op == '-':
        resultat = minus(a, b)
        print(f'{a} - {b} = {resultat}')
    elif op == 'd':
        resultat = durchschnitt(a, b)
        print(f'Durchschnitt von {a} und {b}: {resultat}')
    elif op == 'v':
        resultat = gleiches_vorzeichen(a, b)
        if resultat == True:
            print(f'{a} und {b} haben das gleiche Vorzeichen')
        else:
            print(f'{a} und {b} haben unterschiedliche Vorzeichen')
