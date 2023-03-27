import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_kasvattaminen_toimii(self):
        self.maksukortti.lataa_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 25.00 euroa")

    def test_saldo_vähenee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")


    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_oikean_totuusarvon_true(self):
        totuusarvo=self.maksukortti.ota_rahaa(500)
        self.assertEqual(totuusarvo, True)

    
    def test_metodi_palauttaa_oikean_totuusarvon_false(self):
        totuusarvo=self.maksukortti.ota_rahaa(1500)
        self.assertEqual(totuusarvo, False)
        