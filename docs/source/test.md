# _Tests_



>Da nur die Spiellogik und nicht der Spielablauf und der Computergegner getestet werden soll, 
testen wir die Methoden *setze_spielstein(spielbrett, spalte)*, *gewinn_abfragen()* & *spielbrett_voll()*:



Bei *setze_spielstein(spielbrett, spalte)* testen wir
- das generelle Setzen mit X & O, als auch den Fall, wenn die Spalte (oberster Reihenplatz) schon voll ist. 
(Eine ungültige Spaltennummer per Tastatureingabe wird bereits im Spielablauf der ***Spiel*** Klasse verhindert.)



Bei *gewinn_abfragen()* testen wir



- jeweils die waagrechte, senkrechte & diagonale Möglichkeiten - mit jeweils positiven Gewinnabfragen (4 in einer Reihe, oder auch mehr als 4 - als Sonderfall)
als auch negativen Gewinnabfragen (nur 2 oder 3 in einer Reihe) - für beide Symbole (X,O).



Bei *spielbrett_voll()* testen wir



- dass kein weiterer Zug mehr möglich ist, wenn das Spielbrett (oberste Reihe) schon voll ist und dass das Spiel dann beendet wird (self.abbruch wird dann True).