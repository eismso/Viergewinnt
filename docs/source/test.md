# Tests
Wir testen die Methode setze_spielstein(), gewinn_abfragen() & spielbrett_voll():

bei setze_spielstein() testen wir das generelle Setzen mit X & O, als auch den Fall, wenn die Spalte schon voll ist
bei gewinn_abfragen() testen wir jeweils die waagrechte, senkrechte & diagonale Möglichkeiten - mit jeweils positiven Gewinnabfragen (4 in einer Reihe, oder auch mehr als 4 - als Sonderfall) als auch negativen Gewinnabfragen (nur 2 oder 3 in einer Reihe) - für beide Symbole (X,Y).
bei spielbrett_voll() testen wir, dass kein weiterer Zug mehr möglich ist, wenn das Spielbrett schon voll ist und dass das Spiel dann beendet wird (self.abbruch wird dann False)