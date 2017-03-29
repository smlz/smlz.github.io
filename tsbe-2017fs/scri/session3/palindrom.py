wort = input("Gib ein Wort ein: ")

anzahl_checks = len(wort) // 2

ist_palindrom = True

for i in range(anzahl_checks):
    print("DEBUG:", wort)
    if wort[0] != wort[-1]:
        ist_palindrom = False
        break
    wort = wort[1:-1]

if ist_palindrom:
    print("Bravo")
else:
    print("Leider nein")
