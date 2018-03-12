vorname = input("Vorname? ")
nachname = input("Nachname? ")
per_du = input("Sind wir per du? [j/n] ")[0].lower()

if per_du == 'j':
    anrede = f"Lieber {vorname}"
else:
    anrede = f"Sehr geehrter Herr {vorname} {nachname}"

print(anrede)


