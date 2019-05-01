

liste = [2,1,4367,65,34,1,213,43,5576,32,43,6,537,4,213,4,435]

def quicksort(l):
    print(f"Sortiere die Liste {l}")
    if len(l) <= 1:
        return l
    vergleichswert = l[0]
    kleiner = []
    groesser = []
    for zahl in l[1:]:
        if zahl < vergleichswert:
            kleiner.append(zahl)
        else:
            groesser.append(zahl)
    result = quicksort(kleiner) + [vergleichswert] + quicksort(groesser)
    print(f"Das Resultat {result}")
    return result


assert(quicksort(liste) == sorted(liste))

def retour_zaehlen(zahl):
    if zahl == 0:
        return
    print(zahl)
    retour_zaehlen(zahl - 1)

