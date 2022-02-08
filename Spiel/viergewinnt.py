from typing import List


class Spieler:
    pass


class Spielbrett:

    def __init__(self):
        # hier gleich array erstellen?
        self.feld = []
        self.__anzahl_reihen = 6
        self.__anzahl_spalten = 7
        leerer_eintrag = "   "
        for r in range(self.__anzahl_reihen):
            reihe = []
            for s in range(self.__anzahl_spalten):
                reihe.append(leerer_eintrag)
            self.feld.append(reihe)

    # @property
    # def feld(self):
    #    return self.__feld

    def __repr__(self):
        return f'Spielbrett mit {self.__anzahl_reihen} Reihen und {self.__anzahl_spalten} Spalten'

    def anzeigen(self):
        print('aktuelles Spielbrett: \n')
        for r in range(len(self.feld)):
            print(f'|{self.feld[r][0]}|{self.feld[r][1]}|{self.feld[r][2]}|{self.feld[r][3]}|{self.feld[r][4]}|{self.feld[r][5]}|{self.feld[r][6]}|')
        print('-----------------------------')
        print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')

class Spiel:

    def __init__(self):
        pass

    def starten(self):
        computer = input(f'Möchtest du gegen den Computer spielen? Y/N:')
        # if computer ja etc.
        #TODO: Namen
        pass



if __name__ == '__main__':
    spielbrett = Spielbrett()
    #print(spielbrett.feld[0][0])
    spielbrett.anzeigen()

