def durchschnitt(notenliste):
    summe = 0
    for note in notenliste:
        summe = summe + note
    result = summe / len(notenliste)
    return result

anzahl_noten = int(input("Wie viele Noten hast du? "))
i = 0
noten = []
while i < anzahl_noten:
    note = float(input(f"Welche Note hattest du im Test {i + 1}? "))
 
    if note > 6 or note < 1:
        print("Fehler: Note darf nicht über 6 oder unter 1 sein.")
    else:
        noten.append(note)
        i = i + 1
print("Dein Notenschnitt beträgt:", durchschnitt(noten))
