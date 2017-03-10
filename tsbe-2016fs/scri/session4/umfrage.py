#!/usr/bin/python3

anzahl_fragen = 3
summe = 0
for i in range(anzahl_fragen):
    eingabe = input("Wie schwer fanden sie die Aufgabe {} (1-4)? ".format(i+1))
    summe += int(eingabe)

schnitt = summe / anzahl_fragen

if 1 <= schnitt <= 2:
    schwierigkeit = 'leicht'
elif 2 < schnitt <= 3:
    schwierigkeit = 'mittelschwer'
elif 3 < schnitt <= 4:
    schwierigkeit = 'schwer'
else:
    schwierigkeit = '???'

print("Die Prüfung war für sie {}. (Durchschnitt: {})"
      .format(schwierigkeit, schnitt))
