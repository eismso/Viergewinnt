from typing import List
import random

leerer_eintrag = "   "

class Spielbrett:
    """Erzeugt Spielbrett und zeigt dieses an.

    Die Klasse Spielbrett erzeugt das Spielbrett als nested list mit sieben Spalten und sechs Reihen und zeigt dieses an.

    Attributes
    ----------
    feld: list of list of str
        Gitter des Spielbretts.
    anzahl_reihen: int
        Anzahl der Reihen des Spielbretts.
    anzahl_spalten: int
        Anzahl der Spalten des Spielbretts.
    """
    @property
    def anzahl_reihen(self):
        return self.__anzahl_reihen

    @property
    def anzahl_spalten(self):
        return self.__anzahl_spalten

    def __init__(self):
        self.feld = []
        self.__anzahl_reihen = 6
        self.__anzahl_spalten = 7
        for r in range(self.__anzahl_reihen):
            reihe = []
            for s in range(self.__anzahl_spalten):
                reihe.append(leerer_eintrag)
            self.feld.append(reihe)


    def __repr__(self):
        return f'Spielbrett mit {self.__anzahl_reihen} Reihen und {self.__anzahl_spalten} Spalten'

    def anzeigen(self):
        """Zeigt das aktuelle Spielbrett an.

        Die Funktion zeigt das aktuelle Spielbrett mit dazugehoeriger Spaltennummerierung an.

        Returns
        -------
        Nichts.
        """
        print('\n aktuelles Spielbrett: \n')
        for r in range(len(self.feld)):
            print(f'|{self.feld[r][0]}|{self.feld[r][1]}|{self.feld[r][2]}|{self.feld[r][3]}|{self.feld[r][4]}|{self.feld[r][5]}|{self.feld[r][6]}|')
        print('-----------------------------')
        print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 | \n')

class Spieler:
    """Vergibt die Spielernummer und setzt den Spielstein.

    In der Klasse Spieler erhaelt jeder Spieler eine fortlaufende Nummer und der Spielstein wird gesetzt.

    Attributes
    ----------
    spieler_zaehler: int
        Zaehler der erstellten Spieler.
    name: str
        Name des Spielers.
    spielstein: str
        Spielstein des Spielers.
    spielernummer: int
        Nummer des Spielers.
    """

    __spieler_zaehler = 0

    @property
    def spielernummer(self):
        return self.__spielernummer

    def __init__(self, name: str, spielstein: str):
        self.name = name
        self.spielstein = spielstein
        Spieler.__spieler_zaehler += 1
        self.__spielernummer = Spieler.__spieler_zaehler

    def setze_spielstein(self, spielbrett: Spielbrett, spalte: int) -> bool:
        """Setzt den Spielstein an die richtige Stelle.

        Diese Funktion setzt nach der Eingabe der Spaltennummer den Spielstein in den unterst moeglichen Reihenplatz des Spielbrettes.
        Ueberprueft wird außerdem, ob die Spalte bereits voll ist.
        Wenn dem so ist, kann der Spielstein in dieser Spalte nicht gesetzt werden.
        Nur der oberster Reihenplatz (index 0) der Spalte wird dafuer ueberprueft, weil dieser erst befuellt werden kann,
        wenn die unteren Reihenplaetze schon besetzt sind.

        Parameters
        ----------
        spielbrett: Spielbrett
            Uebergibt das Spielbrett aus der Klasse Spielbrett.
        spalte: int
            Spaltennummer, in die der Stein gesetzt werden soll.

        Returns
        -------
        bool
            True, wenn der Spielstein gesetzt wurde.
        """
        idx_spalte = spalte-1

        if spielbrett.feld[0][idx_spalte] == " X " or spielbrett.feld[0][idx_spalte] == " O ":
            print(f'Spalte {spalte} bereits voll!')
            return False

        spielstein_gesetzt = False
        for r in range(spielbrett.anzahl_reihen -1,-1,-1):
            while (not spielstein_gesetzt) and (spielbrett.feld[r][idx_spalte] == leerer_eintrag):
                if self.spielstein == "X":
                    spielbrett.feld[r][idx_spalte] = " X "
                    spielstein_gesetzt = True
                    return True
                elif self.spielstein == "O":
                    spielbrett.feld[r][idx_spalte] = " O "
                    spielstein_gesetzt = True
                    return True


    def __repr__(self):
        return f'Spieler {self.__spielernummer}: Name = {self.name}, Spielstein = {self.spielstein}'

class Spiel:
    """Steuert den Spielverlauf.

    In der Klasse Spiel wird das Spiel gestartet, die Spielernamen vergeben sowie bei Bedarf der Computergegner aktiviert.
    Nach jedem Spielzug wird das aktuelle Spielbrett angezeigt, es erfolgt eine Gewinnabfrage und es besteht nach dem Spielzug die Moeglichkeit das Spiel abzubrechen.
    Ist das Spielfeld voll, wird das Spiel beendet.

    Attributes
    ----------
    spielbrett: Spielbrett
        Uebergibt das Spielbrett aus der Klasse Spielbrett.
    gewinn: bool
        True, wenn Spiel gewonnen wurde.
    gewinner: str
        Spielstein des Gewinners.
    abbruch: bool
        True, wenn Spiel beendet ist.
    """

    def __init__(self, spielbrett: Spielbrett):
        self.spielbrett = spielbrett
        self.gewinn = False
        self.gewinner = ''
        self.abbruch = False

    def starten(self):
        """Starten des Spiels und Spielablauf.

        Per Tastatureingabe werden die Namen der Spieler erfragt bzw. abgefragt, ob gegen den Computer gespielt werden soll.
        Ebenso wird durch Tastatureingabe die Spaltennummer abgefragt, in der der Spielstein eines Spielers gesetzt werden soll.
        Solange das Spiel nicht abgebrochen wird, wird nach jedem Spielzug das aktuelle Spielbrett angezeigt und eine Gewinnabfrage durchgeführt

        Returns
        -------
        Nichts.
        """
        name = input(f'Hallo! Wie lautet dein Name? : ')
        spieler1 = Spieler(name, "X")
        print(f'Hallo {spieler1.name}! Dein Spielstein ist {spieler1.spielstein}')

        beantwortet = False
        computer_gegner = False
        while not beantwortet:
            computer_abfrage = input(f'Möchtest du gegen den Computer spielen? Y/N:')
            if computer_abfrage == "Y" or computer_abfrage == "y":
                beantwortet = True
                computer_gegner = True
                computer = Spieler("PC", "O")
            elif computer_abfrage == "N" or computer_abfrage == "n":
                name2 = input(f'Hallo! Wie lautet der Name des 2.Spielers? : ')
                spieler2 = Spieler(name2, "O")
                print(f'Hallo {spieler2.name}! Dein Spielstein ist {spieler2.spielstein}')
                beantwortet = True
            else:
                print('Bitte beantworte die Frage mit Y oder N !')

        self.spielbrett.anzeigen()

        while not self.abbruch:
            s1_spielzug = False
            print(f'{spieler1.name} ist an der Reihe!')
            self.weiter_spielen()
            if self.abbruch:
                print('\nSpiel beendet')
                break

            while not s1_spielzug:
                spalte = int(input(f'In welcher Spalte möchstest du deinen Spielstein setzen? : '))
                if (spalte >= 1) and (spalte <= 7):
                    if spieler1.setze_spielstein(self.spielbrett, spalte):
                        s1_spielzug = True
                else:
                    print('Du musst eine Spalte zwischen 1 und 7 angeben!')



            self.spielbrett.anzeigen()
            self.gewinn_abfragen()
            if self.gewinn and (self.gewinner == 'X'):
                print(f'Gratulation! {spieler1.name} hat gewonnen!')
                break
            self.spielbrett_voll()

            if computer_gegner:
                print('Der Computer ist an der Reihe!')
                c_spielzug = False
                while not c_spielzug:
                    spalte_zufall = random.randint(1, 7)
                    if computer.setze_spielstein(self.spielbrett, spalte_zufall):
                        c_spielzug = True
                self.spielbrett.anzeigen()
                self.gewinn_abfragen()
                if self.gewinn and (self.gewinner == 'O'):
                    print(f'Der Computer hat gewonnen!')
                    break
                self.spielbrett_voll()

            if not computer_gegner:
                print(f'{spieler2.name} ist an der Reihe!')
                self.weiter_spielen()
                if self.abbruch:
                    print('\nSpiel beendet')
                    break
                s2_spielzug = False
                while not s2_spielzug:
                    spalte = int(input(f'In welcher Spalte möchstest du deinen Spielstein setzen? : '))
                    if (spalte >= 1) and (spalte <= 7):
                        if spieler2.setze_spielstein(self.spielbrett, spalte):
                            s2_spielzug = True
                    else:
                        print('Du musst eine Spalte zwischen 1 und 7 angeben!')

                self.spielbrett.anzeigen()
                self.gewinn_abfragen()
                if self.gewinn and (self.gewinner == 'O'):
                    print(f'Gratulation! {spieler2.name} hat gewonnen!')
                    break
                self.spielbrett_voll()




    def gewinn_abfragen(self):
        """Ueberprueft, ob ein Gewinn vorliegt.

        Ausgehend von der ersten Position am Spielbrett wird waagrecht, senkrecht und diagonal nach links bzw. diagonal nach rechts ueberprueft,
        ob sich vier gleiche Spielsteine in einer Reihe befinden. Ist das nicht der Fall, erfolgt die Gewinnabfrage – wie für eine for-Schleife ueblich – fuer die naechste Position am Spielbrett.

        Returns
        -------
        Nichts.
        """
        # waagrecht
        for r in range(self.spielbrett.anzahl_reihen -1,-1,-1):
            for s in range(self.spielbrett.anzahl_spalten-3):
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " X " and self.spielbrett.feld[r][s+1] == " X " and self.spielbrett.feld[r][s+2] == " X " and self.spielbrett.feld[r][s+3] == " X ":
                    self.gewinn = True
                    self.gewinner = 'X'
                    self.abbruch = True
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " O " and self.spielbrett.feld[r][s+1] == " O " and self.spielbrett.feld[r][s+2] == " O " and self.spielbrett.feld[r][s+3] == " O ":
                    self.gewinn = True
                    self.gewinner = 'O'
                    self.abbruch = True

        # senkrecht
        for s in range(self.spielbrett.anzahl_spalten):
            for r in range(self.spielbrett.anzahl_reihen -4,-1,-1):
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " X " and self.spielbrett.feld[r+1][s] == " X " and self.spielbrett.feld[r+2][s] == " X " and self.spielbrett.feld[r+3][s] == " X ":
                    self.gewinn = True
                    self.gewinner = 'X'
                    self.abbruch = True
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " O " and self.spielbrett.feld[r+1][s] == " O " and self.spielbrett.feld[r+2][s] == " O " and self.spielbrett.feld[r+3][s] == " O ":
                    self.gewinn = True
                    self.gewinner = 'O'
                    self.abbruch = True

        # diagonal
        # nach rechts
        for s in range(self.spielbrett.anzahl_spalten-3):
            for r in range(self.spielbrett.anzahl_reihen - 1, -1, -1):
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " X " and self.spielbrett.feld[r-1][s+1] == " X " and self.spielbrett.feld[r-2][s+2] == " X " and self.spielbrett.feld[r-3][s+3] == " X ":
                    self.gewinn = True
                    self.gewinner = 'X'
                    self.abbruch = True
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " O " and self.spielbrett.feld[r-1][s+1] == " O " and self.spielbrett.feld[r-2][s+2] == " O " and self.spielbrett.feld[r-3][s+3] == " O ":
                    self.gewinn = True
                    self.gewinner = 'O'
                    self.abbruch = True

        # nach links
        for s in range(self.spielbrett.anzahl_spalten - 4, self.spielbrett.anzahl_spalten):
            for r in range(self.spielbrett.anzahl_reihen - 1, -1, -1):
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " X " and self.spielbrett.feld[r-1][s-1] == " X " and self.spielbrett.feld[r-2][s-2] == " X " and self.spielbrett.feld[r-3][s-3] == " X ":
                    self.gewinn = True
                    self.gewinner = 'X'
                    self.abbruch = True
                while (not self.gewinn) and self.spielbrett.feld[r][s] == " O " and self.spielbrett.feld[r-1][s-1] == " O " and self.spielbrett.feld[r-2][s-2] == " O " and self.spielbrett.feld[r-3][s-3] == " O ":
                    self.gewinn = True
                    self.gewinner = 'O'
                    self.abbruch = True

    def weiter_spielen(self):
        """Ueberprueft, ob das Spiel fortgesetzt werden soll.

        Mittels Tastatureingabe wird abgefragt, ob das Spiel an der jeweiligen Stelle fortgesetzt oder beendet werden soll.

        Returns
        -------
        Nichts.
        """
        abfrage_beantwortet = False
        while not abfrage_beantwortet:
            weiter_abfrage = input(f'Möchtest du weiterspielen? Y/N:')
            if weiter_abfrage == "Y" or weiter_abfrage == "y":
                abfrage_beantwortet = True
            elif weiter_abfrage == "N" or weiter_abfrage == "n":
                self.abbruch = True
                abfrage_beantwortet = True
            else:
                print('Bitte beantworte die Frage mit Y oder N !')

    def spielbrett_voll(self):
        """Ueberprueft, ob das Spielbrett voll ist.

        Ueberprueft, ob das Spielbrett voll ist und keine Steine mehr gesetzt werden koennen. Wenn dem so ist, wird das Spiel beendet.
        Nur die oberste Reihe (index 0) des Spielbretts wird dafuer ueberprueft, weil diese erst befuellt werden kann,
        wenn die unteren Reihenplaetze schon besetzt sind.

        Returns
        -------
        Nichts.
        """
        zaehler = 0
        for s in range(self.spielbrett.anzahl_spalten):
            if self.spielbrett.feld[0][s] == leerer_eintrag:
                zaehler += 1
        if zaehler == 0:
            print('Spielbrett ist voll besetzt, kein weiterer Zug mehr möglich!\nSpiel wird beendet')
            self.abbruch = True



if __name__ == '__main__':
    spielbrett = Spielbrett()
    spiel = Spiel(spielbrett)
    spiel.starten()
