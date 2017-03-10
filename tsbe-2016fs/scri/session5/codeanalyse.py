#!/usr/bin/python3
filename = "codeanalyse.py"   # Dieses Skript selber
with open(filename) as f:
    # Ganzer Dateiinhalt einlesen
    inhalt = f.read()
    zeilen = inhalt.split('\n')
    codezeilen = len(zeilen)
    kommentare = 0
    for zeile in zeilen:
        zeile = zeile.strip()
        if '#' in zeile:
            kommentare += 1

    if kommentare > (codezeilen * 0.6):
        print("Sehr gut dokumentierter Code")
    elif kommentare > (codezeilen * 0.3):
        print("Gut dokumentierter Code")
    else:
        print("Ungenügend dokumentierter Code, bitte nachbessern!")
