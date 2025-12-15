import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_float_calculation(self):
        """
        Tes 5: Uji nilai float yang kompleks.
        Input: 999, Diskon 33%
        Perhitungan manual:
          Diskon = 999 * 0.33 = 329.67
          Harga akhir = 669.33
        """
        hasil = self.calc.hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_edge_case_harga_nol(self):
        """
        Tes 6: Edge Case harga awal 0
        """
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()
