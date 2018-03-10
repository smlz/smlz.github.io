def durch(a, b):
    return a / b

def betrag(a):
    if a < 0:
        resultat = a * (-1)
    else:
        resultat = a
    return resultat

assert(betrag(5) == 5)
assert(betrag(-2.2) == 2.2)

def durchschnitt(a, b):
    return a

assert(durchschnitt(4, 6) == 5)
assert(durchschnitt(4.5, 5) == 4.75)
