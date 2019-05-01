def nichts():
    # Eine Funktion welche nichts macht
    pass


def nicht_viel(x):
    return x


def plus(a, b):
    print(f"Zähle {a} und {b} zusammen")
    erster_summand = a
    zweiter_summand = b
    resultat = erster_summand + zweiter_summand
    return resultat

print("Drei plus vier gibt:", plus(3, 4))
print("Eins plus eins gibt:", plus(1, 1))
