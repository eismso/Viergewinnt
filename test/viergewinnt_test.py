import unittest

from Spiel.viergewinnt import Spielbrett, Spieler, Spiel

class SpielTest(unittest.TestCase):

    def setUp(self) -> None:
        self.spielbrett1 = Spielbrett()
        self.spielbrett_spalte_voll = Spielbrett()
        self.spielbrett_spalte_voll.feld[0][4] = " X "
        self.spielbrett_spalte_voll.feld[0][2] = " O "
        self.spieler1 = Spieler('Hansi', 'X')
        self.spieler2 = Spieler('Franzi', 'O')

        self.spielbrett_waagrecht_vier_X = Spielbrett()
        for s in range(1,5):
            self.spielbrett_waagrecht_vier_X.feld[2][s] = " X "
        self.spiel_waag_vier_X = Spiel(self.spielbrett_waagrecht_vier_X)

        self.spielbrett_waagrecht_vier_O = Spielbrett()
        for s in range(2, 6):
            self.spielbrett_waagrecht_vier_O.feld[4][s] = " O "
        self.spiel_waag_vier_O = Spiel(self.spielbrett_waagrecht_vier_O)

        self.spielbrett_waagrecht_drei_X = Spielbrett()
        for s in range(2, 5):
            self.spielbrett_waagrecht_drei_X.feld[3][s] = " X "
        self.spiel_waag_drei_X = Spiel(self.spielbrett_waagrecht_drei_X)

        self.spielbrett_waagrecht_zwei_O = Spielbrett()
        for s in range(0, 2):
            self.spielbrett_waagrecht_zwei_O.feld[1][s] = " O "
        self.spiel_waag_zwei_0 = Spiel(self.spielbrett_waagrecht_zwei_O)

        self.spielbrett_waagrecht_fuenf_X = Spielbrett()
        for s in range(2, 7):
            self.spielbrett_waagrecht_fuenf_X.feld[3][s] = " X "
        self.spiel_waag_fuenf_X = Spiel(self.spielbrett_waagrecht_fuenf_X)






    def test_setze_spielstein(self):
        erg1 = self.spieler1.setze_spielstein(self.spielbrett1, 4)
        erg2 = self.spieler2.setze_spielstein(self.spielbrett1, 6)
        erg3 = self.spieler1.setze_spielstein(self.spielbrett_spalte_voll, 5)
        erg4 = self.spieler2.setze_spielstein(self.spielbrett_spalte_voll, 3)
        self.assertTrue(erg1)
        self.assertTrue(erg2)
        self.assertFalse(erg3)
        self.assertFalse(erg4)

    def test_gewinn_abfragen_waagrecht(self):
        self.spiel_waag_vier_X.gewinn_abfragen()
        self.assertTrue(self.spiel_waag_vier_X.gewinn)
        self.spiel_waag_vier_O.gewinn_abfragen()
        self.assertTrue(self.spiel_waag_vier_O.gewinn)
        self.spiel_waag_drei_X.gewinn_abfragen()
        self.assertFalse(self.spiel_waag_drei_X.gewinn)
        self.spiel_waag_zwei_0.gewinn_abfragen()
        self.assertFalse(self.spiel_waag_zwei_0.gewinn)
        self.spiel_waag_fuenf_X.gewinn_abfragen()
        self.assertTrue(self.spiel_waag_fuenf_X.gewinn)



if __name__ == '__main__':
    unittest.main()
