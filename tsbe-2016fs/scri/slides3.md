class: center, middle
# Scripting 3

TSBE Frühlingssemester 2016  
`http://smlz.github.io/tsbe-2016fs/scri/`  

Marco Schmalz  
`marco.schmalz@gibb.ch`  
  
.footnote.bottom[<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/assets/cc88x31.png" /></a>]

---
## Kursübersicht

1. Bash und UNIX-Tools

2. Einführung in Python 

3. **Python: Datei und Prozessoperationen**

4. Python Generatoren

5. Repetition
---
# Heute

1. Test

2. Repetition

3. Funktionen und Rekursion

4. File I/O

5. Externe Kommandos ausführen

---
# Nichts

.center[
```python
None

pass
```
]


`None`: Ein fixer Wert, welcher "Nichts" bedeutet.

`pass`: Ein Statement (Befehl), welches nichts macht.

---

# Zahlen

* Rechenoperatoren: `+ - * / // % **`

* Vergleiche: `== != > < >= >=`

* Konvertieren: 

  * Ganzzahl: `int("42")`
  
  * Reelle Zahl: `float("3.1459")`
  
---

# Booleans

* `True`

* `False`

* Verknüpfungen: `not and or`

---
# Strings

* Literals: `"String eins" 'String "zwei"'`

* Mehrzeilig:
```python
lyrics = """You wake up late for school man you don't wanna go
You ask you mom, "Please?" but she still says, "No!"
You missed two classes and no homework
But your teacher preaches class like you're some kind of jerk"""
```
* Einzelner Buchstabe: `"Hallo"[1]`

* Substring: `"Fasten"[1:4]`

* Auftrennen:
```python
>>> "Fest gemauert in der Erden / Steht die".split()
['Fest', 'gemauert', 'in', 'der', 'Erden', '/', 'Steht', 'die']
>>> "Fest gemauert in der Erden / Steht die".split('/')
['Fest gemauert in der Erden ', ' Steht die']
```
---
# String-Formatting

* Einfach:
```python
>>> "{} {}".format(3014, "Bern")
'3014 Bern'
```

* Positionen:
```python
>>> "{1}, {0}".format("George", "Harrison")
'Harrison, George'
```

* Keywords:
```python
>>> "{vorname} {nachname}".format(nachname="Urlaub", vorname="Farin")
'Farin Urlaub'
```

---
# Listen

* Zugriff auf Elemente
```python
>>> l = [1, 2, 3, 4, 5]
>>> l[1]
2
>>> l[-1]
5
```

* Unterlisten
```python
>>> l[2:4]
[3, 4]
>>> l[1:-2]
[2, 3]
>>> l[1:]
[2, 3, 4, 5]
>>> l[:3]
[1, 2, 3]
```
---
# Listen (cont.)

* Elemente hinzufügen
```python
>>> l = []
>>> l.append(1)
>>> l.append("zwei")
>>> l.append(3.0)
>>> l
[1, 'zwei', 3.0]
```

* Elemente zu einem einzigen String convertieren:
```python
>>> namen = ['Julia', 'Levi', 'Emira', 'Kyle']
>>> print('\n'.join(namen))
Julia
Levi
Emira
Kyle
```
