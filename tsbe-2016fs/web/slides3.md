class: center, middle
# Web-Programmieren 3

TSBE Frühlingssemester 2016  
`http://smlz.github.io/tsbe-2016fs/web/`  

Marco Schmalz  
`marco.schmalz@gibb.ch`  



.footnote.bottom.smaller[<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/assets/cc88x31.png" width="88" height="31" /></a>]
---
## Kursübersicht

1. HTML und CSS, Bootstrap

2. Repetition HTML/CSS, JavaScript Einführung

3. **AngularJS Browser-Applikation**

4. (Auffahrt)

5. Backend mit Elasticsearch
---
# Heute

1. Test

2. Projektarbeit

3. Angular Einführung

---
class: center
# Tutorial

http://www.codecademy.com/en/tracks/javascript

---
# Angular template

```javascript
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>AngularJS Plunker</title>
  <script data-require="angular.js@1.3.x" data-semver="1.3.6"
  src="https://code.angularjs.org/1.3.6/angular.js"></script>
  <script>
  var app = angular.module('itApp', []);
  app.controller('TodoController', TodoController);
  function TodoController() {
    var self = this;
    self.name = "Hans";
  }  
  </script>
</head>
<body ng-app="itApp">
  <div ng-controller="TodoController as ctrl">
    <p ng-bind="ctrl.name"></p>
    <p>{{ctrl.name}}</p>
  </div>
</body>
</html>
```



