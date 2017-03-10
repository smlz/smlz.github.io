#!/usr/bin/python3

import csv

filename = 'mitglieder.csv'

for mitglied in csv.DictReader(open(filename)):
    # Frage: Wie lauten die Emailadressen der Mitglieder die noch nicht
    # bezahlt haben?
    print(mitglied['Vorname'], mitglied['Nachname'])


# Idealer Output: "Vorname1 Nachame1" <email1@example.com>, "Vorname2 ...
