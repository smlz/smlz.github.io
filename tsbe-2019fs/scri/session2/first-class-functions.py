
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mal(a, b):
    return a * b


def zeige_berechnung(a, b, funktion):
    print(f"Berechnung der Funktion '{funktion.__name__}' mit {a} und {b}")
    resultat = funktion(a, b)
    print(f"Das Resultat ist '{resultat}'")


zeige_berechnung(7, 6, plus)
zeige_berechnung(6, 7, mal)
