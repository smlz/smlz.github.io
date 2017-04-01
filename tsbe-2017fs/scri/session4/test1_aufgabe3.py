#!/usr/bin/python3.6

test_nummern = [1, 2]
total = 0

for test_nummer in test_nummern:
    # Hier vervollständigen: ...
    note =  float(input(f"Was war deine Note im Test {test_nummer}? "))

    # Überprüfe, ob die Note zwischen 1 und 6 liegt. ...
    if not 1 <= note <= 6:
        print("Ungültige Note:", note)
        note = 1

    total = total + note

print("Dein Notenschnitt beträgt:", total / len(test_nummern))
