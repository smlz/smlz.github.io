class: center, middle
# Web-Programmieren 1

TSBE Frühlingssemester 2017  
`http://smlz.github.io/tsbe-2017fs/web/`  

Marco Schmalz  
`marco.schmalz@gibb.ch`  

.footnote.bottom[<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/assets/by-sa.svg" /></a>]
---
# Kursübersicht

1. **Einführung, HTML und CSS, Twitter Bootstrap, Projektstart**

2. UX-Design, Repetition HTML/CSS, Einführung JavaScript

3. JavaScript, Bindings/Vue, Projektarbeit

4. Routing, einfaches Backend, Projektarbeit

5. Elasticsearch, Präsentationen, Praxistipps

---
# Heute

1. Einführung HTML

2. Gruppenarbeit zu HTML-Tags

3. Wettbewerb

4. Einführung CSS

5. CSS-Tutorial

6. Bootstrap

7. Projektstart (auf Papier)

---
class: center
# HTML als Baumstruktur

![](html-tree.png)

---
# Ressourcen zu HTML

* Mozilla Developer Network: https://developer.mozilla.org/

  Bei Google *MDN* zum Suchbegriff eingeben.

* SelfHTML Wiki (Deutsch): https://wiki.selfhtml.org/

---

# Gruppenarbeit: HTML-Tags

* 4 Gruppen

* Grundstruktur einer Webseite

* Links

* Bilder einbetten

* Listen und Tabellen

---
class: center, middle
#Wettbewerb:<br/> 90er-Jahre Webseite
---
# Tim Berners-Lee

.middle.center[![Tim Berners-Lee](tbl.jpg)]

.center[Das World Wide Web wurde 1989 in der Schweiz am CERN erfunden.]
---
# CSS

* Formateigenschaften beschreiben die Formatierung

* Der CSS-Selektor beschreibt, auf welches Element die Formatierung angewandt wird.
---

# CSS-Selektoren: <br/>Einfache Elemente

####CSS  
```CSS
*td {
    border: solid black 2px;
}
```
####HTML
```HTML
<table>
  <tr>
*     <td >Diese Zelle hat einen Rand</td>
*     <td>... und diese auch!</td>
  </tr>
</table>
```
---
# CSS-Selektoren: <br/>Klassen

####CSS
```CSS
*td.mitRand {
    border: solid black 2px;
}
```
####HTML
```HTML
<table>
  <tr>
*     <td class="mitRand">Diese Zelle hat einen Rand</td>
      <td>... und diese keinen!</td>
  </tr>
</table>
```
---
# CSS-Selektoren: <br/>Geschachtelte Elemente

####CSS
```CSS
*table.mitRand td {
    border: solid black 2px;
}
```
####HTML
```HTML
<table class="mitRand">
  <tr>
*     <td>Diese Zelle hat einen Rand</td>
  </tr>
</table>
<table>
  <tr>
      <td>... und diese keinen!</td>
  </tr>
</table>
```
---
# CSS-Selektoren: <br/>Direkte Kinder

####CSS
```CSS
*table > tr > td {
    border: solid black 2px;
}
```
####HTML
```HTML
<table>
  <th>
    <td>Kein Rand hier :-(</td>
  <th>
  <tr>
*      <td class="mitRand">Dafür hier</td>
  </tr>
</table>
```
---
# CSS-Selektoren: <br/>Geschwister

####CSS
```CSS
*td.mitRand, td.mitRand + td {
    border: solid black 2px;
}
```
####HTML
```HTML
<table>
  <tr>
*     <td class="mitRand">Diese Zelle hat einen Rand</td>
*     <td>... und diese auch!</td>
  </tr>
</table>
```
---
# CSS-Selektoren: IDs

####CSS
```CSS
*#mitRand {
    border: solid black 2px;
}
```
####HTML
```HTML
<table>
  <tr>
*     <td id="mitRand">Diese Zelle hat einen Rand</td>
      <td>... und hier wieder mal keiner!</td>
  </tr>
</table>
```

ID-Attribute haben in einem HTML einen speziellen Status, denn sie dürfen in
jedem Dokument genau einmal verwendet werden.

---
# Tutorial

http://www.codecademy.com/courses/css-coding-with-style/

Vor allem Kapitel 3: Precision Targeting with Classes and Selectors

---
# Projekt

* 2er- oder 3er-Teams

* Idee erarbeiten: Zum Beispiel Wettplattform

* Beispiele

  * [Zum Runden Leder](http://blog.derbund.ch/zumrundenleder/blog/2014/06/23/115357/)

  * http://www.kicktipp.de/zrl14-15/tabellen

---
# Anforderungen: Job Stories

* **Wenn** SITUATIONSBESCHRIEB,
* **möchte ich** MOTIVATION,
* **damit** ERGEBNIS.

Beispiel:
```
Wenn der Beutel meines Roboterstaubsauger fast (also ca. 90%) voll ist,
möchte ich eine Mitteilung auf das Handy kriegen,
damit ich rechtzeitig neue Säcke kaufen kann.
```

* **Auftrag**:
 * Zweierteams bilden
 * Sich für eine Projektvariante entscheiden
 * Zusammen vier Job-Stories schreiben

* Zusatzinfos: [Replacing The User Story With The Job Story](https://medium.com/the-job-to-be-done/replacing-the-user-story-with-the-job-story-af7cdee10c27)

---
# Screen Designs ...

.center[![UI Sketch](ui-sketches.jpg)]

---
# ... auf Papier


** Auftrag **

* Diskutiert, wie ihr eure Applikation in maximal 3 Screens unterbringt

* Zeichnet die Screens auf Papier und spielt die Anwendung durch

* Umsetzung ...

---
# Bootstrap

 * Von Twitter entwickelt

 * "Quasi-Standard"

 * Dokumentation:

    * http://holdirbootstrap.de/css/

    * http://holdirbootstrap.de/komponenten/
---
# Bootstrap benutzten

```HTML
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <title>Bootstrap Vorlage</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
  <body>
    <h1>Hello world!</h1>

    <!-- Hier kommt unser Code -->

    <!-- Bootstrap JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js">
    </script>
  </body>
</html>
```
