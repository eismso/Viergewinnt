from typing import List


class Spieler:
    pass


class Spielbrett:

    def __init__(self):
        # hier gleich array erstellen?
        self.feld = []
        self.__anzahl_reihen = 6
        self.__anzahl_spalten = 7
        leerer_eintrag = "|   |"
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

    def show(self):
        #TODO: mit f-strings schöner ausgeben
        #TODO: noch Zahlenreihe hinzufügen
        for r in self.feld:
            print(r)
        print('----------------------------------------------------------------')


class Spiel:

    def __init__(self):
        pass

    def starten(self):
        computer = input(f'Möchtest du gegen den Computer spielen? Y/N:')
        # if computer ja etc.
        pass



if __name__ == '__main__':
    spielbrett = Spielbrett()
    print(spielbrett.feld[0][0])
    print(spielbrett)
    spielbrett.feld[1]
    spielbrett.show()
