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
        print(x)
  
    return "-".join(woerter)

assert(ziffern_als_wort([1, 2, 3]) == 'eins-zwei-drei')
