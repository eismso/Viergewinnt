import unittest

from Spiel.viergewinnt import Spielbrett, Spieler, Spiel


class SpielTest(unittest.TestCase):

    def setUp(self) -> None:
        # setUp für Spielstein setzen
        self.spielbrett1 = Spielbrett()
        self.spiel_leeres_spielbrett = Spiel(self.spielbrett1)
        self.spielbrett2 = Spielbrett()
        self.spielbrett2.feld[5][3] = " X "
        self.spielbrett2.feld[4][3] = " O "
        self.spielbrett_spalte_voll = Spielbrett()
        self.spielbrett_spalte_voll.feld[0][4] = " X "
        self.spielbrett_spalte_voll.feld[0][2] = " O "
        self.spieler1 = Spieler('Hansi', 'X')
        self.spieler2 = Spieler('Franzi', 'O')

        # setUp für waagrechte Gewinnabfrage
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

        #setUp für senkrechte Gewinnabfrage
        self.spielbrett_senk_vier_X = Spielbrett()
        for r in range(2, 6):
            self.spielbrett_senk_vier_X.feld[r][3] = " X "
        self.spiel_senk_vier_X = Spiel(self.spielbrett_senk_vier_X)

        self.spielbrett_senk_vier_O = Spielbrett()
        for r in range(0, 4):
            self.spielbrett_senk_vier_O.feld[r][0] = " O "
        self.spiel_senk_vier_O = Spiel(self.spielbrett_senk_vier_O)

        self.spielbrett_senk_drei_X = Spielbrett()
        for r in range(2, 5):
            self.spielbrett_senk_drei_X.feld[r][4] = " X "
        self.spiel_senk_drei_X = Spiel(self.spielbrett_senk_drei_X)

        self.spielbrett_senk_zwei_O = Spielbrett()
        for r in range(0, 2):
            self.spielbrett_senk_zwei_O.feld[r][1] = " O "
        self.spiel_senk_zwei_0 = Spiel(self.spielbrett_senk_zwei_O)

        self.spielbrett_senk_fuenf_X = Spielbrett()
        for r in range(1, 6):
            self.spielbrett_senk_fuenf_X.feld[r][6] = " X "
        self.spiel_senk_fuenf_X = Spiel(self.spielbrett_senk_fuenf_X)

        # setUp für diagonal nach rechts - Gewinnabfrage
        self.spielbrett_diagr_vier_X = Spielbrett()
        self.spielbrett_diagr_vier_X.feld[4][3] = " X "
        self.spielbrett_diagr_vier_X.feld[3][4] = " X "
        self.spielbrett_diagr_vier_X.feld[2][5] = " X "
        self.spielbrett_diagr_vier_X.feld[1][6] = " X "
        self.spiel_diagr_vier_X = Spiel(self.spielbrett_diagr_vier_X)

        self.spielbrett_diagr_vier_O = Spielbrett()
        self.spielbrett_diagr_vier_O.feld[5][0] = " O "
        self.spielbrett_diagr_vier_O.feld[4][1] = " O "
        self.spielbrett_diagr_vier_O.feld[3][2] = " O "
        self.spielbrett_diagr_vier_O.feld[2][3] = " O "
        self.spiel_diagr_vier_O = Spiel(self.spielbrett_diagr_vier_O)

        self.spielbrett_diagr_drei_X = Spielbrett()
        self.spielbrett_diagr_drei_X.feld[2][4] = " X "
        self.spielbrett_diagr_drei_X.feld[1][5] = " X "
        self.spielbrett_diagr_drei_X.feld[0][6] = " X "
        self.spiel_diagr_drei_X = Spiel(self.spielbrett_diagr_drei_X)

        self.spielbrett_diagr_zwei_O = Spielbrett()
        self.spielbrett_diagr_zwei_O.feld[3][1] = " O "
        self.spielbrett_diagr_zwei_O.feld[2][2] = " O "
        self.spiel_diagr_zwei_0 = Spiel(self.spielbrett_diagr_zwei_O)

        self.spielbrett_diagr_fuenf_X = Spielbrett()
        self.spielbrett_diagr_fuenf_X.feld[4][2] = " X "
        self.spielbrett_diagr_fuenf_X.feld[3][3] = " X "
        self.spielbrett_diagr_fuenf_X.feld[2][4] = " X "
        self.spielbrett_diagr_fuenf_X.feld[1][5] = " X "
        self.spielbrett_diagr_fuenf_X.feld[0][6] = " X "
        self.spiel_diagr_fuenf_X = Spiel(self.spielbrett_diagr_fuenf_X)

        # setUp für diagonal nach links - Gewinnabfrage
        self.spielbrett_diagl_vier_X = Spielbrett()
        self.spielbrett_diagl_vier_X.feld[5][6] = " X "
        self.spielbrett_diagl_vier_X.feld[4][5] = " X "
        self.spielbrett_diagl_vier_X.feld[3][4] = " X "
        self.spielbrett_diagl_vier_X.feld[2][3] = " X "
        self.spiel_diagl_vier_X = Spiel(self.spielbrett_diagl_vier_X)

        self.spielbrett_diagl_vier_O = Spielbrett()
        self.spielbrett_diagl_vier_O.feld[3][3] = " O "
        self.spielbrett_diagl_vier_O.feld[2][2] = " O "
        self.spielbrett_diagl_vier_O.feld[1][1] = " O "
        self.spielbrett_diagl_vier_O.feld[0][0] = " O "
        self.spiel_diagl_vier_O = Spiel(self.spielbrett_diagl_vier_O)

        self.spielbrett_diagl_drei_X = Spielbrett()
        self.spielbrett_diagl_drei_X.feld[4][5] = " X "
        self.spielbrett_diagl_drei_X.feld[3][4] = " X "
        self.spielbrett_diagl_drei_X.feld[2][3] = " X "
        self.spiel_diagl_drei_X = Spiel(self.spielbrett_diagl_drei_X)

        self.spielbrett_diagl_zwei_O = Spielbrett()
        self.spielbrett_diagl_zwei_O.feld[3][2] = " O "
        self.spielbrett_diagl_zwei_O.feld[2][1] = " O "
        self.spiel_diagl_zwei_0 = Spiel(self.spielbrett_diagl_zwei_O)

        self.spielbrett_diagl_fuenf_X = Spielbrett()
        self.spielbrett_diagl_fuenf_X.feld[5][6] = " X "
        self.spielbrett_diagl_fuenf_X.feld[4][5] = " X "
        self.spielbrett_diagl_fuenf_X.feld[3][4] = " X "
        self.spielbrett_diagl_fuenf_X.feld[2][3] = " X "
        self.spielbrett_diagl_fuenf_X.feld[1][2] = " X "
        self.spiel_diagl_fuenf_X = Spiel(self.spielbrett_diagl_fuenf_X)

        # setUp für spielbrett_voll()-Test
        self.spielbrett_voll = Spielbrett()
        for s in range(self.spielbrett_voll.anzahl_spalten):
            self.spielbrett_voll.feld[0][s] = " X "
        self.spiel_spielbrett_voll = Spiel(self.spielbrett_voll)
        self.spielbrett_freier_eintrag = Spielbrett()
        for s in range(0, 6):
            self.spielbrett_voll.feld[0][s] = " O "
        self.spiel_freier_eintrag = Spiel(self.spielbrett_freier_eintrag)


    def test_setze_spielstein(self):
        erg1 = self.spieler1.setze_spielstein(self.spielbrett1, 4)
        erg2 = self.spieler2.setze_spielstein(self.spielbrett1, 6)
        erg3 = self.spieler1.setze_spielstein(self.spielbrett_spalte_voll, 5)
        erg4 = self.spieler2.setze_spielstein(self.spielbrett_spalte_voll, 3)
        erg5 = self.spieler1.setze_spielstein(self.spielbrett2, 4)
        self.assertTrue(erg1)
        self.assertTrue(erg2)
        self.assertFalse(erg3)
        self.assertFalse(erg4)
        self.assertTrue(erg5)
        self.assertEqual(self.spielbrett2.feld[3][3], " X ")

    def test_gewinn_abfragen_waagrecht(self):
        self.spiel_waag_vier_X.gewinn_abfragen()
        self.assertTrue(self.spiel_waag_vier_X.gewinn)
        self.spiel_waag_vier_O.gewinn_abfragen()
        self.assertTrue(self.spiel_waag_vier_O.gewinn)
        self.spiel_waag_drei_X.gewinn_abfragen()
        self.assertFalse(self.spiel_waag_drei_X.gewinn)
        self.spiel_waag_zwei_0.gewinn_abfragen()
        self.assertFalse(self.spiel_waag_zwei_0.gewinn)
        self.assertFalse(self.spiel_waag_zwei_0.abbruch)
        self.assertEqual(self.spiel_waag_zwei_0.gewinner, '')
        self.spiel_waag_fuenf_X.gewinn_abfragen()
        self.assertTrue(self.spiel_waag_fuenf_X.gewinn)
        self.assertTrue(self.spiel_waag_fuenf_X.abbruch)
        self.assertEqual(self.spiel_waag_fuenf_X.gewinner, 'X')

    def test_gewinn_abfragen_senkrecht(self):
        self.spiel_senk_vier_X.gewinn_abfragen()
        self.assertTrue(self.spiel_senk_vier_X.gewinn)
        self.spiel_senk_vier_O.gewinn_abfragen()
        self.assertTrue(self.spiel_senk_vier_O.gewinn)
        self.assertTrue(self.spiel_senk_vier_O.abbruch)
        self.assertEqual(self.spiel_senk_vier_O.gewinner, 'O')
        self.spiel_senk_drei_X.gewinn_abfragen()
        self.assertFalse(self.spiel_senk_drei_X.gewinn)
        self.assertFalse(self.spiel_senk_drei_X.abbruch)
        self.assertEqual(self.spiel_senk_drei_X.gewinner, '')
        self.spiel_senk_zwei_0.gewinn_abfragen()
        self.assertFalse(self.spiel_senk_zwei_0.gewinn)
        self.spiel_senk_fuenf_X.gewinn_abfragen()
        self.assertTrue(self.spiel_senk_fuenf_X.gewinn)

    def test_gewinn_abfragen_diagonal_rechts(self):
        self.spiel_diagr_vier_X.gewinn_abfragen()
        self.assertTrue(self.spiel_diagr_vier_X.gewinn)
        self.assertTrue(self.spiel_diagr_vier_X.abbruch)
        self.assertEqual(self.spiel_diagr_vier_X.gewinner, 'X')
        self.spiel_diagr_vier_O.gewinn_abfragen()
        self.assertTrue(self.spiel_diagr_vier_O.gewinn)
        self.spiel_diagr_drei_X.gewinn_abfragen()
        self.assertFalse(self.spiel_diagr_drei_X.gewinn)
        self.assertFalse(self.spiel_diagr_drei_X.abbruch)
        self.assertEqual(self.spiel_diagr_drei_X.gewinner, '')
        self.spiel_diagr_zwei_0.gewinn_abfragen()
        self.assertFalse(self.spiel_diagr_zwei_0.gewinn)
        self.spiel_diagr_fuenf_X.gewinn_abfragen()
        self.assertTrue(self.spiel_diagr_fuenf_X.gewinn)

    def test_gewinn_abfragen_diagonal_links(self):
        self.spiel_diagl_vier_X.gewinn_abfragen()
        self.assertTrue(self.spiel_diagl_vier_X.gewinn)
        self.spiel_diagl_vier_O.gewinn_abfragen()
        self.assertTrue(self.spiel_diagl_vier_O.gewinn)
        self.assertTrue(self.spiel_diagl_vier_O.abbruch)
        self.assertEqual(self.spiel_diagl_vier_O.gewinner, 'O')
        self.spiel_diagl_drei_X.gewinn_abfragen()
        self.assertFalse(self.spiel_diagl_drei_X.gewinn)
        self.spiel_diagl_zwei_0.gewinn_abfragen()
        self.assertFalse(self.spiel_diagl_zwei_0.gewinn)
        self.assertFalse(self.spiel_diagl_zwei_0.abbruch)
        self.assertEqual(self.spiel_diagl_zwei_0.gewinner, '')
        self.spiel_diagl_fuenf_X.gewinn_abfragen()
        self.assertTrue(self.spiel_diagl_fuenf_X.gewinn)

    def test_spielbrett_voll(self):
        self.spiel_spielbrett_voll.spielbrett_voll()
        self.assertTrue(self.spiel_spielbrett_voll.abbruch)
        self.spiel_leeres_spielbrett.spielbrett_voll()
        self.assertFalse(self.spiel_leeres_spielbrett.abbruch)
        self.spiel_freier_eintrag.spielbrett_voll()
        self.assertFalse(self.spiel_leeres_spielbrett.abbruch)



if __name__ == '__main__':
    unittest.main()
