from typing import List

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
        print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')

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

    def __init__(self, spielbrett: Spielbrett):
        spielbrett = spielbrett

    def starten(self):
        computer = input(f'Möchtest du gegen den Computer spielen? Y/N:')
        # if computer ja etc.
        #TODO: Namen
        pass

    def gewinn_abfragen(self):

        gewinn = False

        # waagrecht
        for r in range(spielbrett.anzahl_reihen -1,-1,-1):
            for s in range(spielbrett.anzahl_spalten-3):
                #if self.spielstein == "X":
                while (not gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r][s+1] == " X " and spielbrett.feld[r][s+2] == " X " and spielbrett.feld[r][s+3] == " X ":
                    gewinn = True

                while (not gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r][s+1] == " O " and spielbrett.feld[r][s+2] == " O " and spielbrett.feld[r][s+3] == " O ":
                    gewinn = True

        # senkrecht
        for s in range(spielbrett.anzahl_spalten):
            for r in range(spielbrett.anzahl_reihen -4,-1,-1):

                while (not gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r+1][s] == " X " and spielbrett.feld[r+2][s] == " X " and spielbrett.feld[r+3][s] == " X ":
                    gewinn = True

                while (not gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r+1][s] == " O " and spielbrett.feld[r+2][s] == " O " and spielbrett.feld[r+3][s] == " O ":
                    gewinn = True

        # diagonal
        for s in range(spielbrett.anzahl_spalten-3):
            for r in range(spielbrett.anzahl_reihen - 1, -1, -1):
                # nach rechts
                while (not gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r-1][s+1] == " X " and spielbrett.feld[r-2][s+2] == " X " and spielbrett.feld[r-3][s+3] == " X ":
                    gewinn = True

                while (not gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r-1][s+1] == " O " and spielbrett.feld[r-2][s+2] == " O " and spielbrett.feld[r-3][s+3] == " O ":
                    gewinn = True

                # nach links
                while (not gewinn) and spielbrett.feld[r][s] == " X " and spielbrett.feld[r-1][s-1] == " X " and spielbrett.feld[r-2][s-2] == " X " and spielbrett.feld[r-3][s-3] == " X ":
                    gewinn = True

                while (not gewinn) and spielbrett.feld[r][s] == " O " and spielbrett.feld[r-1][s-1] == " O " and spielbrett.feld[r-2][s-2] == " O " and spielbrett.feld[r-3][s-3] == " O ":
                    gewinn = True

        if gewinn:
            print("\n Spiel gewonnen!")



if __name__ == '__main__':
    spielbrett = Spielbrett()
    print(spielbrett)
    spielbrett.anzeigen()

    spieler1 = Spieler("Hansi", "X")
    print(spieler1)
    spieler2 = Spieler("Franz", "O")
    print(spieler2)

    # test für spielstein setzen
    spieler1.setze_spielstein(spielbrett,2)
    spielbrett.anzeigen()
    spieler2.setze_spielstein(spielbrett, 2)
    spielbrett.anzeigen()

