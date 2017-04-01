wahl = ''

eintraege = [
    {'Vorname': 'Andreas', 'Nachname': 'Megert'},
    {},
    {},
    {},
]

felder = "Vorname Nachname Telefon".split()

def bearbeiten(eintrag):
    eintrag['Vorname'] = input('Vorname: ').strip()
    eintrag['Nachname'] = input('Nachname: ').strip()
    eintrag['Telefon'] = input('Telefon: ').strip()

def anzeigen(eintrag):
    print('Vorname:  ', eintrag.get('Vorname'))
    print('Nachname: ', eintrag.get('Nachname'))
    print('Telefon:  ', eintrag.get('Telefon'))


while wahl != 'q':
    print("Was willst du machen?")
    print("[b] Eintrag bearbeiten")
    print("[a] Eintrag abfragen")
    print("[q] Beenden")

    wahl = input('> ').strip()[0].lower()  # Nur der erste Buchstabe lowercase interessiert

    if wahl == 'b':
        index = int(input("Welchen Eintrag (Index)? "))
        bearbeiten(eintraege[index])
    elif wahl == 'a':
        index = int(input("Welchen Eintrag (Index)? "))
        anzeigen(eintraege[index])
