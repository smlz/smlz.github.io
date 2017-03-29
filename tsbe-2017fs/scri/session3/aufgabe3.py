wahl = ''

eintrag = {'Vorname': 'Andreas', 'Nachname': 'Megert'}

felder = "Vorname Nachname Telefon".split()

while wahl != 'q':
    print("Was willst du machen?")
    print("[b] Eintrag bearbeiten")
    print("[a] Eintrag abfragen")
    print("[q] Beenden")

    wahl = input('> ').strip()[0].lower()  # Nur der erste Buchstabe lowercase interessiert

    if wahl == 'b':
        eintrag['Vorname'] = input('Vorname: ').strip()
        eintrag['Nachname'] = input('Nachname: ').strip()
        eintrag['Telefon'] = input('Telefon: ').strip()
    elif wahl == 'a':
        print('Vorname:  ', eintrag.get('Vorname'))
        print('Nachname: ', eintrag.get('Nachname'))
        print('Telefon:  ', eintrag.get('Telefon'))
