ziffern = "null eins zwei drei vier fünf sechs sieben acht neun".split()

def ziffer_als_wort(ziffer):
    if 0 <= ziffer < 10:
        return ziffern[ziffer]
    else:
        return "error"

assert(ziffer_als_wort(1) == 'eins')
assert(ziffer_als_wort(7) == 'sieben')


def ziffern_als_wort(ziffern):
    woerter = []
    for x in ziffern:
        woerter.append(ziffer_als_wort(x))

    return "-".join(woerter)

liste_mit_zahlen = [1, 2, 3]
resultat = ziffern_als_wort(liste_mit_zahlen)
assert(resultat == 'eins-zwei-drei')
