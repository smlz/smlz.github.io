# while loop der solange läuft, bis der user 'quit' eingibt

kantone =  {
    'GR': {
        'name': 'Graubünden',
        'hauptort': 'Chur',
        'einwohner': 430000,
        'sprachen': ['de', 'rm', 'it'],
    },
    'BE': {
        'name': 'Bern', #...
    },
}

sprachen = {'de': 'Deutsch', 'fr': 'Französisch', 'it': 'Italienisch', 'rm': 'Romanisch'}

running = True
while running:
    kuerzel = input("Zu welchem Kanton möchtest du Informationen? ")
    kuerzel = kuerzel.strip().upper()
    if kuerzel in "QUIT Q EXIT X".split():
        running = False
    elif kuerzel in kantone:
        kanton = kantone[kuerzel]
        name = kanton.get('name', kuerzel)
        print(f"Informationen zum Kanton {name}:")
        if 'hauptort' in kanton:
            print(f"   * Hauptort: {kanton['hauptort']}")
        #if kuerzel in einwohner:
        #    print(f"   * Einwohnerzahl: {einwohner[kuerzel]}")
        if 'sprachen' in kanton:
            schoenere_sprachen = []
            for code in kanton['sprachen']:
                schoenere_sprachen.append(sprachen[code])

            sprachen_string = ', '.join(schoenere_sprachen)

            print(f"   * Amtssprachen: {sprachen_string}")



