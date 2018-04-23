adressen = []
f = open('adressen.csv')
for zeile in f:
    adressen.append(zeile.strip().split(','))
f.close()

def anzeigen():
    for vorname, name, email in adressen:
        print(f"{vorname} {name}: {email}")

def hinzufuegen():
    vorname = input("Vorname: ")
    name = input("Nachname: ")
    email = input("Email: ")
    adressen.append([vorname, name, email])
    speichern()

def speichern():
    f = open('adressen.csv', 'w')
    for eintrag in adressen:
        print(",".join(eintrag), file=f)

def suche():
    resultate = []
    begriff = input("Nach was möchtest du suchen? ").lower()
    for eintrag in adressen:
        treffer = False
        for feld in eintrag:
            if begriff in feld.lower():
                treffer = True
        if treffer:
            resultate.append(eintrag)

    if len(resultate) == 0:
        print("Keine Resultate")
    else:
        print(f"{len(resultate)} Treffer:")
        for vorname, name, email in resultate:
            print(f"{vorname} {name}: {email}")

done = False
while not done:
    print("""Optionen:
    - Alles anzeigen [a]
    - Eintrag hinzufügen [h]
    - Suchen [s]
    - Beenden [q]""")
    eingabe = input("Was möchtest du tun? ").strip().lower()

    if eingabe == 'a':
        anzeigen()
    elif eingabe == 'h':
        hinzufuegen()
    elif eingabe == 's':
        suche()
    elif eingabe == 'q':
        done = True
    else:
        print("Ungültige Eingabe\n")
