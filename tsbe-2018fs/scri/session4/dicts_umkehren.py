de_fr = {
    'Hund': 'chien',
    'Katze': 'chat',
    'Wein': 'vin',
    'Bier': 'bierre',
    'Liebe': 'amour',
}


fr_de = {} # TODO

running = True
while running:
    eingabe = input("Deutsch-Französisch: 1, Französisch-Deutsch: 2 ? ").strip()
    if eingabe.lower() in "exit x quit q".split():
        running = False
    elif eingabe == '1':
        deutsch = input("Wort auf Deutsch: ")
        if deutsch in de_fr:
            print(de_fr[deutsch])
        else:
            print("Wort nicht gefunden")
    elif eingabe == '2':
        franz = input("Wort auf Französisch: ")
        if franz in fr_de:
            print(fr_de[franz])
        else:
            print("Wort nicht gefunden")

