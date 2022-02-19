# Beschreibung der Implementierung

Ausgehend von den Fragen „Wie kann das Spielbrett angelegt werden und wie soll es aussehen?“, „Wie kann ein Spielstein gesetzt werden?“ 
und „Wie kann das Spiel gestartet bzw. gewonnen werden?“ wurde der Code in drei Klassen aufgeteilt.
In der Klasse „Spielbrett“ wird das Spielfeld mit Hilfe eines Arrays erstellt. Für eine bessere Darstellung werden die Spalten mit „|“ getrennt 
und für die später klarere Eingabe für die Spieler die Spalten mit Spaltennummern versehen.

In der Klasse „Spieler“ erhalten die Spieler eine fortlaufende Nummer. Diese Klasse enthält auch die Funktion des Setzens eines Spielsteins.
Hierfür (wie auch später bei der Gewinnabfrage) wurde eine Kombination aus for- und while-Schleife gewählt:
Ausgehend von der eingegebenen Spalte (Achtung: Index daher eingegebene Spalte – 1) wird Reihe für Reihe überprüft,
ob ein Feld leer ist. Im ersten leeren Feld, das gefunden wird, wird der Spielstein gesetzt.

In der Klasse „Spiel“ geht es um den konkreten Spielablauf: Der Spieler wird zunächst nach dem Namen gefragt 
und kann entweder gegen den Computer oder gegen einen anderen Spieler spielen. 
Nach jedem Spielzug wird das aktuelle Spielbrett ausgegeben und eine Gewinnabfrage durchgeführt. 
Wie beim Setzen des Spielsteines wird auch bei der Gewinnabfrage eine Kombination aus for- und while-Schleife verwendet:
Ausgehend von der „Stelle 0“ wird waagrecht, senkrecht und diagonal nach links bzw. diagonal nach rechts überprüft,
ob sich vier gleichfarbige Steine in einer Reihe finden. Ist das nicht der Fall erfolgt die Gewinnabfrage – wie für eine for-Schleife üblich – 
für die nächste Stelle.
Gibt es (noch) keinen Gewinner kann das Spiel nach jedem Spielzug abgebrochen werden, oder es kann weitergespielt werden.
Ist das Spielfeld voll, wird das Spiel ohne Gewinner beendet. 
