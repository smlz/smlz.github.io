class: center, middle
# Scripting 2

TSBE Frühlingssemester 2017  
`http://smlz.github.io/tsbe-2016fs/scri/`  

Marco Schmalz  
`marco.schmalz@gibb.ch`  

.footnote.bottom[<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/assets/by-sa.svg" /></a>]

---
## Kursübersicht

1. Tools, Zahlen, Strings und Entscheidungen

2. **Mehr Strings, Listen und Schleifen**

3. dicts und Funktionen

4. Files und externe Kommandos

5. Praxistipps, externe Libraries und Repetition
---
# Heute

1. Repetition

2. Strings

3. Listen

4. Loops

---
## Interaktiver Python Modus

Den interaktiven Modus erreicht man, indem man Python ohne weitere Parameter aufruft. Die drei grösser-als-Zeichen (`>>>`) zeigen an, dass wir uns im interaktiven Modus befinden.

```
$ python3.6
>>> 1 + 1
2
>>> "Hallo" + " " + "Welt" + "!"
'Hallo Welt!'
>>> True or False
True
>>> "Birnen" == "Äpfel"
False
>>> quit()
```

Der interaktive Modus eignet sich sehr gut, um ein kurzes Codestück zu testen, oder um kurz auszuprobieren, ob etwas in Python so funktioniert.

---
## Ein Python-Skript schreiben


1. Eine Datei mit der Endung **.py** erstellen.

2. Python-Code in die Datei schreiben. Bsp.: `mein_programm.py`
```python
print("Die Antwort zum Leben, dem Universum und allem:")
print(42)
```
3. Die Datei ausführen, indem man Python mit dem Dateinamen als Parameter aufruft:
```bash
$ python3.6 mein_programm.py
Die Antwort zum Leben, dem Universum und allem:
42
```
---
## Rechnen in Python

```python
>>> 3 + 4
7
>>> 2 * 5
10
>>> 2 ** 10    # Hoch
1024
>>> 5 / 2
2.5
>>> 1.5 - 0.5
1.0
>>> 7 // 3     # Ganzzahlige Division
2
>>> 7 % 2      # Rest der Division (Modulo)
1
>>> (3 + 5) * 2 - 1
15
```
---
## Zahlen

Zwei Arten

1. Ganzzahlen
  * Können beliebig gross werden
  * Bsp.: `-1` oder `42`

2. Fliesskommazahlen
  * Bsp.: `2.7` oder `-15.2`


---
## Dingen einen Namen geben

```python
duo = 2

trio = 3

pi = 3.14159

e = 2.718281828459045

vorname = "Frieda"

nachname = "Müller"

geschlecht = "w"

hat_ein_auto = True

mag_hunde = False
```

In Python sind keine Typendeklarationen nötig.

---
## Text: Strings

```python
vorname = 'Franz'
nachname = "Klammer"
brille ="O'Neil"
fahrstil = """
* elegant
* geschmeidig
* schnell
"""
```

Länge von Strings:
```
>>> len('abc')
3
```
---
## Printing

```
>>> print("Hallo", "Welt!")
Hallo Welt!
>>> print("Eins", 2, 'drei', 4.0)
Eins 2 drei 4.0
>>> print(1, 2, 3, sep=";")
1;2;3
>>> print("Hallo", end="-")        # keine neue Zeile beginnen
Hallo->>>
```
---
## Printing in eine Datei

```python
f = open("meine_datei.txt", 'w')    
# 'w' (write) für (Über-)Schreiben, 'a' (append) zum Anhängen

print("Liebe Oma", file=f)
...

f.close()
```


---

## Benutzereingaben abfragen

`input()` gibt eine Benutzereingabe zurück

Bsp.:
```python
name = input("Wie heisst du? ")

print("Hallo", name)
```

---
## Text zu Zahl kovertieren

* Einen String in eine Ganzzahl konvertieren: `int`
```python
>>> zahl = int("42")
>>> zahl
42
```
* Einen String in eine Fliesskommazahl konvertieren: `float`
```python
>>> zahl = float("-2.7")
>>> zahl
-2.7
```


---
## Verzweigungen: if

```python
alter = 24

if alter < 16:
    print("Du musst noch viel lernen!")
elif alter > 65:
    print("Nie wieder arbeiten!")
else:
    print("An die Arbeit!")
```
---
## Vergleiche und logische Operatoren

- `==`: gleich
- `!=`: ungleich
- `is`: identisch
- `> `: grösser
- `< `: kleiner
- `>=`: grösser-gleich
- `<=`: kleiner-gleich


- `and`: Und-Verknüpfung (beide Bedingungen müssen erfüllt sein)
- `or `: Oder-Verknüpfung (mindestens eine Bedingung muss erfüllt sein)
- `not`: Negierung

```python
if alter >= 18 or alter < 65:
    print("Leider kein Rabatt")
```
