vorname = input("Dein Vorname: ")
nachname = input("Dein Nachname: ")
wohnort = input("Dein Wohnort: ")

print(f"Lieber {vorname}, ist es schön in {wohnort}?")

f = open("adressbuch.csv", "a")    # An die Datei anhängen

print(vorname, nachname, wohnort, sep=",", file=f)

f.close()

#with open(..) as f:
#    print(..., file=f)     # Schliesst file automatisch


