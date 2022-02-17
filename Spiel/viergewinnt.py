from typing import List
import random

leerer_eintrag = "   "

class Spielbrett:

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
        print('\n aktuelles Spielbrett: \n')
        for r in range(len(self.feld)):
            print(f'|{self.feld[r][0]}|{self.feld[r][1]}|{self.feld[r][2]}|{self.feld[r][3]}|{self.feld[r][4]}|{self.feld[r][5]}|{self.feld[r][6]}|')
        print('-----------------------------')
        print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 | \n')

class Spieler:

    __spieler_zaehler = 0

    @property
    def spielernummer(self):
        return self.__spielernummer

    def __init__(self, name: str, spielstein: str):
        self.name = name
        self.spielstein = spielstein
        Spieler.__spieler_zaehler += 1
        self.__spielernummer = Spieler.__spieler_zaehler

    def setze_spielstein(self, spielbrett: Spielbrett, spalte: int):
        idx_spalte = spalte-1
        spielstein_gesetzt = False
        for r in range(spielbrett.anzahl_reihen -1,-1,-1):
            while (not spielstein_gesetzt) and (spielbrett.feld[r][idx_spalte] == leerer_eintrag):
                if self.spielstein == "X":
                    spielbrett.feld[r][idx_spalte] = " X "
                    spielstein_gesetzt = True
                elif self.spielstein == "O":
                    spielbrett.feld[r][idx_spalte] = " O "
                    spielstein_gesetzt = True

    def __repr__(self):
        return f'Spieler {self.__spielernummer}: Name = {self.name}, Spielstein = {self.spielstein}'

class Spiel:

    gewinn = False
    gewinner = ''

    def __init__(self, spielbrett: Spielbrett):
        self.spielbrett = spielbrett

    def starten(self):
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
            elif computer_abfrage == "N" or computer_abfrage =="n":
                name2 = input(f'Hallo! Wie lautet der Name des 2.Spielers? : ')
                spieler2 = Spieler(name2, "O")
                print(f'Hallo {spieler2.name}! Dein Spielstein ist {spieler2.spielstein}')
                beantwortet = True
            else:
                print('Bitte beantworte die Frage mit Y oder N !')

        self.spielbrett.anzeigen()

        while not Spiel.gewinn:
            s1_spielzug = False
            print(f'{spieler1.name} ist an der Reihe!')
            while not s1_spielzug:
                spalte = int(input(f'In welcher Spalte möchstest du deinen Spielstein setzten? : '))
                if (spalte >= 1) and (spalte <= 7):
                    spieler1.setze_spielstein(self.spielbrett, spalte)
                    s1_spielzug = True
                else:
                    print('Du musst eine Spalte zwischen 1 und 7 angeben!')

            self.spielbrett.anzeigen()
            self.gewinn_abfragen()
            if Spiel.gewinn and (Spiel.gewinner == 'X'):
                print(f'Gratulation! {spieler1.name} hat gewonnen!')
                break

            if computer_gegner:
                print('Der Computer ist an der Reihe!')
                spalte_zufall = random.randint(1, 7)
                computer.setze_spielstein(self.spielbrett, spalte_zufall)
                self.spielbrett.anzeigen()
                self.gewinn_abfragen()
                if Spiel.gewinn and (Spiel.gewinner == 'O'):
                    print(f'Der Computer hat gewonnen!')



            if not computer_gegner:
                print(f'{spieler2.name} ist an der Reihe!')
                s2_spielzug = False
                while not s2_spielzug:
                    spalte = int(input(f'In welcher Spalte möchstest du deinen Spielstein setzten? : '))
                    if (spalte >= 1) and (spalte <= 7):
                        spieler2.setze_spielstein(self.spielbrett, spalte)
                        s2_spielzug = True
                    else:
                        print('Du musst eine Spalte zwischen 1 und 7 angeben!')

                self.spielbrett.anzeigen()
                self.gewinn_abfragen()
                if Spiel.gewinn and (Spiel.gewinner == 'O'):
                    print(f'Gratulation! {spieler2.name} hat gewonnen!')

    def gewinn_abfragen(self):
        # waagrecht
        for r in range(spielbrett.anzahl_reihen -1,-1,-1):
            for s in range(spielbrett.anzahl_spalten-3):
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r][s+1] == " X " and spielbrett.feld[r][s+2] == " X " and spielbrett.feld[r][s+3] == " X ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'X'
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r][s+1] == " O " and spielbrett.feld[r][s+2] == " O " and spielbrett.feld[r][s+3] == " O ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'O'

        # senkrecht
        for s in range(spielbrett.anzahl_spalten):
            for r in range(spielbrett.anzahl_reihen -4,-1,-1):
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r+1][s] == " X " and spielbrett.feld[r+2][s] == " X " and spielbrett.feld[r+3][s] == " X ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'X'
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r+1][s] == " O " and spielbrett.feld[r+2][s] == " O " and spielbrett.feld[r+3][s] == " O ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'O'

        # diagonal
        for s in range(spielbrett.anzahl_spalten-3):
            for r in range(spielbrett.anzahl_reihen - 1, -1, -1):
                # nach rechts
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r-1][s+1] == " X " and spielbrett.feld[r-2][s+2] == " X " and spielbrett.feld[r-3][s+3] == " X ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'X'
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r-1][s+1] == " O " and spielbrett.feld[r-2][s+2] == " O " and spielbrett.feld[r-3][s+3] == " O ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'O'

                # nach links
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r-1][s-1] == " X " and spielbrett.feld[r-2][s-2] == " X " and spielbrett.feld[r-3][s-3] == " X ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'X'
                while (not Spiel.gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r-1][s-1] == " O " and spielbrett.feld[r-2][s-2] == " O " and spielbrett.feld[r-3][s-3] == " O ":
                    Spiel.gewinn = True
                    Spiel.gewinner = 'O'




if __name__ == '__main__':
    spielbrett = Spielbrett()
    spiel = Spiel(spielbrett)
    spiel.starten()

