
import math  
from datetime import datetime

class KalkulatorLingkaran:
    def __init__(self, radius):
        self.__radius = 0
        self.set_radius(radius)
        print(f"Objek lingkaran dengan radius {self.__radius} dibuat.")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Error: Radius harus lebih besar dari 0.")
            self.__radius = 1  

    def hitung_luas(self):
        luas = math.pi * (self.__radius ** 2)
        return luas

    def hitung_keliling(self):
        keliling = 2 * math.pi * self.__radius
        return keliling


lingkaran_1 = KalkulatorLingkaran(7)

luas_lingkaran = lingkaran_1.hitung_luas()
keliling_lingkaran = lingkaran_1.hitung_keliling()

print(f"\nRadius: {7}")
print(f"Luas Lingkaran: {luas_lingkaran:.2f}")      
print(f"Keliling Lingkaran: {keliling_lingkaran:.2f}")

class LogPesan :
    def __init__(self,pengirim, isi_pesan):
        self.__pengirim = pengirim
        self.__isi_pesan = isi_pesan
        self.__timestamp = datetime.now()

    def tampilkan_log(self):
        waktu_terhormat = self.__timestamp.strftime("%d %B %Y, Pukul %H:%M:%S")
        print("--- Log Pesan Masuk ---")
        print(f"Pengirim : {self.__pengirim}")
        print(f"Waktu :  {waktu_terhormat}")
        print(f"Pesan :  {self.__isi_pesan}")

pesan_1 = LogPesan("Admin", "Server akan segera di-restart untuk maintenance.")
pesan_1.tampilkan_log()

pesan_2 = LogPesan("User01", "Pekerjaan saya sudah disimpan, silahkan restart.")
pesan_2.tampilkan_log()
