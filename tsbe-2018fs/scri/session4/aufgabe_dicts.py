# while loop der solange läuft, bis der user 'quit' eingibt

kantone = {'BL': 'Basel Landschaft', 'GR': 'Graubünden', 'BE': 'Bern'}
hauptorte = {'BL': 'Liestal', 'GR': 'Chur', 'BE': 'Bern', 'VD': 'Lausanne'}
einwohner = {'BL': 220000, 'GR': 430000, 'BE': 1000000, 'AI': 16000}
amtssprachen = {'BL': ['de'], 'GR': ['de', 'rm', 'it'], 'BE': ['de', 'fr']}
sprachen = {'de': 'Deutsch', 'fr': 'Französisch', 'it': 'Italienisch', 'rm': 'Romanisch'}

running = True
while running:
    kuerzel = input("Zu welchem Kanton möchtest du Informationen? ")
    kuerzel = kuerzel.strip().upper()
    if kuerzel in "QUIT Q EXIT X".split():
        running = False
    else:
        kanton = kantone.get(kuerzel, kuerzel)
        print(f"Informationen zum Kanton {kanton}:")
        if kuerzel in hauptorte:
            print(f"   * Hauptort: {hauptorte[kuerzel]}")
        if kuerzel in einwohner:
            print(f"   * Einwohnerzahl: {einwohner[kuerzel]}")
        if kuerzel in amtssprachen:
            #print(f"   * Amtssprachen:")
            schoenere_sprachen = []
            for code in amtssprachen[kuerzel]:
                #print(f"     - {sprachen[code]}")
                schoenere_sprachen.append(sprachen[code])

            print(f"   * Amtssprachen:", ', '.join(schoenere_sprachen))



