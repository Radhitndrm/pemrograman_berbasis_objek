from bangun_datar.lingkaran import Lingkaran
from bangun_datar.persegi import Persegi

def jalankan_program():
    print("--- Menghitung Luas Bangun Datar (Versi Modular) ---")

    lingkaran_A = Lingkaran(7)
    luas_lingkaran = lingkaran_A.hitung_luas()
    print(f"Luas Lingkaran dengan radius 7 adalah {luas_lingkaran:.2f}")

    persegi_B = Persegi(5)
    luas_persegi = persegi_B.hitung_luas()
    print(f"Luas Persegi dengan sisi 5 adalah {luas_persegi}")

if __name__ == "__main__":
    jalankan_program()
