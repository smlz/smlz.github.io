zahl = 10

while zahl > 0:
    print(f"Zahl {zahl} immer noch grösser als 0")
    zahl -= 1

zahl = 2134996

def ziffern_einer_zahl(zahl):
    ziffern = []
    while zahl > 0:
        rest = zahl % 10
        ziffern.append(rest)
        zahl = zahl // 10  # Ganzzahldivision
    ziffern.reverse()
    return ziffern

namen_von_ziffern = 'null eins zwei drei vier fünf sechs sieben acht neun'.split()

def zahl_in_woertern(zahl):
    ziffern = ziffern_einer_zahl(zahl)
    woerter = []
    for ziffer in ziffern:
        woerter.append(namen_von_ziffern[ziffer])
    return '-'.join(woerter)
