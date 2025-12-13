import math

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * (self.radius ** 2)

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2


print("--- Menghitung Luas Bangun Datar (Versi Monolitik) ---")

lingkaran_A = Lingkaran(7)
luas_lingkaran = lingkaran_A.hitung_luas()
print(f"Luas Lingkaran dengan radius 7 adalah {luas_lingkaran:.2f}")

persegi_B = Persegi(5)
luas_persegi = persegi_B.hitung_luas()
print(f"Luas Persegi dengan sisi 5 adalah {luas_persegi}")
