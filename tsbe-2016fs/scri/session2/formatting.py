#!/usr/bin/python3

print("Wie heisst du?")
vorname = input()

plz_ok = False
while not plz_ok:
   plz = input('PLZ? ')
   try:
     plz = int(plz)
     if plz < 1000 or plz >= 10000:
       print('PLZ ungültig')
     else:
       plz_ok = True
   except ValueError:
     print('Ungültige Zahl')
print('Hallo', vorname)
print('Deine PLZ:', plz)


