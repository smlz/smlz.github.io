kantone = {
  'Bern': 'BE',
  'Waadt': 'VD',
  'Appenzell Ausserrhoden': 'AR',
  'Wallis': 'VS',
}
hauptorte = {
  'BE': 'Bern',
  'VD': 'Lausanne',
  'AR': 'Herisau',
  'SG': 'St. Gallen',
}

# 1. Gib für alle Kantone den jeweiligen Hauptort aus
# Waadt: Lausanne

for kantonsname, kuerzel in kantone.items():
    # print(kantonsname, kuerzel)
    if kuerzel in hauptorte:
        print(kantonsname, hauptorte[kuerzel])

# 2. Mach einen neuen Dict, in welchem man den Kantonsnamen für jeden Hauptort
# nachschauen kann.

kanton_fuer_hauptorte = {}

for kantonsname, kuerzel in kantone.items():
    if kuerzel in hauptorte:
        hauptort = hauptorte[kuerzel]   # Wert aus dem dict hauptorte holen
        kanton_fuer_hauptorte[hauptort] = kantonsname # Wert in dict updaten

# Als Einzeiler mit dict-comprenensions
kanton_fuer_hauptorte = { hauptorte[kuerzel]: kanton
                          for kanton, kuerzel in kantone.items()
                          if kuerzel in hauptorte }

print(kanton_fuer_hauptorte)

for hauptort, kantonsname in kanton_fuer_hauptorte.items():
    print(f"{hauptort} ist der Hauptort des Kantons {kantonsname}")
