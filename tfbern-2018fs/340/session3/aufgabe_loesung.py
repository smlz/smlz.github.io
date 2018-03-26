
kantone = {
    'VS': 'Wallis',
}

amtssprachen = {
    'VS': ['de', 'fr'],
}

sprachen = {'de': 'Deutsch', 'rm': 'Romanisch', 'fr': 'Französisch'}

hauptorte = {'VS': 'Sion'}

done = False

while not done:
    eingabe = input("Über welchen Kanton möchtest du gerne mehr erfahren? ").strip()

    if eingabe.lower() in ['quit', 'q', 'exit', 'x']:
        done = True
    else:
        kuerzel = eingabe.upper()
        name = kantone.get(kuerzel, kuerzel)
        print(f"Informationen zum Kanton {name}:")
        if kuerzel in hauptorte:
            print(f" * Hauptort: { hauptorte[kuerzel] }")
        if kuerzel in amtssprachen:
            sprachen_liste = [sprachen[code] for code in amtssprachen[kuerzel]]
            sprachen_str = ", ".join(sprachen_liste)
            print(f" * Amtssprachen: {sprachen_str}")
