
kantone = {
    'VS': 'Wallis',
}

amtssprachen = {
    'VS': ['de', 'fr'],
}

sprachen = {'de': 'Deutsch', 'rm': 'Romanisch'}

hauptorte = {}

done = False

while not done:
    eingabe = input("Über welchen Kanton möchtest du gerne mehr erfahren? ")

    if eingabe.lower() in ['quit', 'q', 'exit', 'x']:
        done = True
    else:
        pass   # TODO: Informationen zum Kanton ausgeben, falls vorhanden
        # Überprüfen ob ein Stichwort in einem dict vorkommt: 'stichwort' in dict
