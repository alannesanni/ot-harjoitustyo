import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa=Kassapaate()
        self.kortti=Maksukortti(1000)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 )
        
    def test_edulliset_alussa_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0 )

    def test_maukkaat_alussa_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0 )


    def test_kateisosto_tarpeeksi_rahaa_edullinen(self):
        vaihtoraha=self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 260)


    def test_kateisosto_tarpeeksi_rahaa_maukas(self):
        vaihtoraha=self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_ei_tarpeeksi_rahaa_edullinen(self):
        vaihtoraha=self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)

    def test_kateisosto_ei_tarpeeksi_rahaa_maukas(self):
        vaihtoraha=self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 300)

    def test_edullinen_maksukortti_tarpeeksi_rahaa(self):
        arvo=self.kassa.syo_edullisesti_kortilla(self.kortti)    
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(arvo, True)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_maksukortti_tarpeeksi_rahaa(self):
        arvo=self.kassa.syo_maukkaasti_kortilla(self.kortti)    
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(arvo, True)
        self.assertEqual(self.kassa.maukkaat, 1)


    def test_edullinen_maksukortti_ei_tarpeeksi_rahaa(self):
        kortti=Maksukortti(100)
        arvo=self.kassa.syo_edullisesti_kortilla(kortti)    
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(arvo, False)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukas_maksukortti_ei_tarpeeksi_rahaa(self):
        kortti=Maksukortti(100)
        arvo=self.kassa.syo_maukkaasti_kortilla(kortti)    
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(arvo, False)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_rahan_lataus_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 15.00 euroa")
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)

    def test_negatiivinen_rahan_lataus_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    