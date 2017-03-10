#!/usr/bin/python3
filename = input("Gebe einen Dateiname an: ")
zu_lang = 0
limit = 80

def zeilenlaengen(filename):
    f = open(filename)
    inhalt = f.read()
    zeilen = inhalt.split('\n')

    zeilenlaengen = []

    for zeile in zeilen:
        laenge = len(zeile)
        zeilenlaengen.append(laenge)

    f.close()
    return zeilenlaengen

for i, laenge in enumerate(zeilenlaengen(filename), start=1):
    if laenge > limit:
        zu_lang += 1
        print("Zeile {} ist zu lang!".format(i))

print("Die Datei '{}' enthält {} zu lange Zeilen.".format(filename, zu_lang))
