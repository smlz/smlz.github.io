ziffern = "null eins zwei drei vier fünf sechs sieben acht neun".split()

def ziffer_als_wort(ziffer):
    if 0 <= ziffer < 10:
        return ziffern[ziffer]
    else:
        return "error"

assert(ziffer_als_wort(1) == 'eins')
assert(ziffer_als_wort(7) == 'sieben')
