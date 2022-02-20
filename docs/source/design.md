# _Beschreibung der Implementierung_

---

Ausgehend von den Fragen

- „Wie kann das Spielbrett angelegt werden und wie soll es aussehen?“

- „Wie kann ein Spielstein gesetzt werden?“ und „Wie kann das Spiel gestartet bzw. gewonnen werden?“ wurde der Code in drei Klassen aufgeteilt.





>In der Klasse ***Spielbrett*** wird das Spielfeld mit Hilfe einer *nested list* erstellt. Für eine bessere Darstellung werden die Spalten mit „|“ getrennt 
und für die später klarere Eingabe für die Spieler die Spalten mit Spaltennummern versehen.

>In der Klasse ***Spieler*** erhalten die Spieler eine fortlaufende Nummer und ihren Namen sowie ihren Spielstein zugewiesen.
Diese Klasse enthält auch die Funktion des Setzens eines Spielsteins. 
Hierfür (wie auch später bei der Gewinnabfrage) wurde eine Kombination aus for- und while-Schleife gewählt: 
Ausgehend von der eingegebenen Spalte (Achtung: Index = eingegebene Spalte – 1) wird Reihe für Reihe überprüft, 
ob ein Feld leer ist. Im ersten leeren Feld, das gefunden wird, wird der Spielstein als *String* gesetzt.

>In der Klasse ***Spiel*** geht es um den konkreten Spielablauf: Der Spieler wird per Tastatureingabe zunächst nach dem Namen gefragt 
und kann entweder gegen den Computer oder gegen einen anderen Spieler spielen. 
Nach jedem Spielzug (Setzen des Spielsteins) wird das aktuelle Spielbrett ausgegeben, eine Gewinnabfrage durchgeführt und überprüft, ob das Spielbrett schon voll ist. 
Wie beim Setzen des Spielsteines wird auch bei der Gewinnabfrage eine Kombination aus for- und while-Schleife verwendet: 
Ausgehend von der ersten Position des Spielbretts wird waagrecht, senkrecht und diagonal nach links bzw. diagonal nach rechts überprüft, 
ob sich vier gleichfarbige Steine in einer Reihe finden. Ist das nicht der Fall erfolgt die Gewinnabfrage – wie für eine for-Schleife üblich – 
für die nächste Stelle.

Gibt es (noch) keinen Gewinner kann das Spiel nach jedem Spielzug abgebrochen werden, oder es kann weitergespielt werden. 
Wenn das Spielbrett voll ist, können keine Steine mehr gesetzt werden und das Spiel wird beendet.
