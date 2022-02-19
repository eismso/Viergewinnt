# Design Pattern

---

## _Memento_

Memento ist ein Entwurfsmuster, welches zur Sorte der Verhaltensmuster zählt. Es dient unter anderem zur Erfassung und der Externalisierung des internen Zustands eines Objektes. Es ist ein sogenanntes GoF-Muster. Es speichert den vorherigen Zustand eines Objektes und kann diesen wiederherstellen, ohne die Details seiner Implementierung preiszugeben.

Man verwendet das Memento-Verhaltensmuster wenn man beispielsweise eine Momentaufnahme des Zustands eines Objektes zwischenspeichern muss oder wenn verhindert werden soll, dass eine direkte Schnittstelle zur Ermittlung des Zustands Implementierungsdetails offenlegt

Es besteht aus Originator, Memento und Verwalter, der Originator ist ein Objekt mit internem Zustand, der verändert werden kann. Im Memento wird dieser Zustand gespeichert und kann später wieder abgerufen werden. Der Verwalter weiß Herkunft und Datum des Zustandes und weiß auch wann der Zustand wiederhergestellt werden soll.



### Wie ist es zu implementieren?

>Zuerst bestimmt man welche Klasse die Rolle des Urhebers übernehmen soll.

>Danach wird die Memento-Klasse erstellt. Nacheinander folgt die Deklarierung der Reihen von Feldern, die in der Urheberklasse deklarierte Felder widerspiegeln.

>Die Memento-Klasse wird dann unveränderlich implementiert. Ein Memento sollte die Daten nur einmal über den Konstruktor annehmen. Die Klasse sollte keinen Setter besitzen.

>Im besten Fall sollte die Klasse innerhalb des Urhebers verschachtelt werden. Danach fügt man der Urheberklasse eine Methode zum Erstellen von Erinnerungsstücken zu.

>Dieser Klasse sollte man eine Methode zum Wiederherstellen des Zustandes des Urhebers hinzufügen.

>Der Verwalter weiß wann er neue Erinnerungsstücke vom Urheber anfordern muss.



### Vorteile des Memento Design Pattern

```sh

Man kann Momentaufnahmen des Zustands eines Objekts erstellen, ohne eine Verkapselung zu verletzen

Man kann den Code des Urhebers vereinfachen, indem man dem Verwalter die Verwaltung über Verlauf des Zustands überlässt.

```
![Memento Pattern](https://upload.wikimedia.org/wikipedia/commons/3/38/W3sDesign_Memento_Design_Pattern_UML.jpg "Memento Pattern")
---
## State Pattern
---
Das State Pattern gehört zu den Design Patterns, die sich mit dem Verhalten von Klassen beschäftigen. 
>Durch Anwendung des State Patterns ändert ein Objekt sein Verhalten, je nachdem welchen Zustand ein Objekt hat.
Es wird der Anschein erweckt, dass das Objekt seine Klasse verändert.

### Problem
---
Zustandsabhängiges Verhalten wird generell mit vielen bedingten Anweisungen (*if-else* oder *switch*) implementiert. 
Wenn mehr Zustände und zustandsabhängiges Verhalten hinzugefügt werden sollen, entstehen extra lange und komplexe bedingte Anweisungen, um das entsprechende Verhalten auswählen zu können.
Außerdem führt jede Veränderung, die die Übergänge zw. den Zuständen betrifft, dazu, dass jede bedingte Anweisung jeder Methode diesbezüglich überprüft werden muss.

### Lösung
---
**Das zustandsabhängige Verhalten wird abgekapselt**: 
- für jeden Zustand wird eine eigene Klasse angelegt (***Konkrete Zustände***)
- ein Interface (***State***) wird mit den zustandsabhängigen abstrakten Methoden angelegt
- Klassen implementierten Interface 
- die ***Kontext*** Klasse 
    - beinhaltet eine Referenz auf eine Zustandsklasse, die den aktuellen Zustand definiert
    - und delegiert das zuständige Verhalten an das aktuellen Zustandsobjekt
- um den Zustand zu ändern, wird das aktuelle Zustandsobjekt mit einem Objekt des neuen Zustandes mithilfe des Interface ausgetauscht

### Vorteile
---
```sh
- ersetzt extra lange und komplexe bedingte Anweisungen
- Flexibilität und Wiederverwendbarkeit
- neue Zustände und Übergange können leicht hinzugefügt werden
- dynamisches Verhalten
```

### Nachteile
---
```sh
- zu aufwendig, 
    wenn es nur wenige Zustände gibt 
    oder diese sich selten verändern
- erhöht die Anzahl an Klassen
```

### UML Diagramm
---
![State Pattern in UML](https://upload.wikimedia.org/wikipedia/commons/9/90/State_Design_Pattern_UML_Class_Diagram.png "State Pattern in UML")

---
## Decorator
---
### Ausgangslage
---
Ein Programm sendet Benachrichtigungen über wichtige Ereignisse an eine vom Klienten vordefinierte Mailingliste. 
Die Nutzer*innen möchten nun aber nicht nur mehr per E-Mail benachrichtigt werden, sondern auch per SMS, Facebook oder 
über eine Slack Benachrichtigung. Zudem werden die unterschiedlichsten Benachrichtigungs-Kombinationen gewünscht bis hin
zu Benachrichtigungen auf allen vier Kanälen. All diese potentiellen Benachrichtigungskombinationen rein über die 
Implementierung von Subklassen abzubilden, würde den Rahmen jedes Codes sprengen:

![Vererbungsexpolsion](https://refactoring.guru/images/patterns/diagrams/decorator/problem3.png?id=f3b3e7a107d870871f2c "Vererbungsexplosion")

Bei der Vererbung stößt man hier an seine Grenzen, da diese für diesen Fall zu statisch ist. Außerdem können Subklassen 
nur eine Elternklasse besitzen. Eine Klasse kann also nicht die Verhaltensweisen mehrerer Klassen erben.

Daher empfiehlt es sich in diesem Fall anstelle der Vererbung einen Decorator zu verwenden: Mit diesem kann man 
eine Klasse um zusätzliche Funktionalitäten erweitern. Als Real-World Analogie kann das Sich-Warm-Anziehen gesehen 
werden: Wenn es einem kalt ist, zieht man einen Pullover an. Wenn es einem noch immer kalt ist eine Jacke. Wenn es 
regnet zieht man eine Regenjacke darüber. Mit diesen zusätzlichen Schichten erweitert man sein ursprüngliches 
„Basisrepertoire“. Es ist aber auch auf einfache Art und Weise möglich eine Schicht bzw. eine Funktionalität auch 
wieder wegzulassen.

## Struktur eines Decorators
---
Die Komponente stellt die Schnittstelle für Wrapper und dekoriertem Objekt dar. Die konkrete Komponente definiert 
die Klasse von Objekten, die umhüllt werden und definiert das zu verändernde Verhalten. Die Basis-Decorator-Klasse 
verweist auf das zu dekorierende Objekt und delegiert alle Operationen an das umschlossene Objekt. Die konkrete 
Decorator Klasse definiert die zusätzlichen Verhaltensweisen. Der Client kann Komponenten in mehrere, dekorierende 
Schichten einhüllen.

## Quellen
---
https://refactoring.guru/design-patterns/decorator

https://de.wikipedia.org/wiki/Decorator

