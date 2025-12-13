
from datetime import datetime

# Class Film (Enkapsulasi)
class Film:
    def __init__(self, judul, harga_tiket, kursi_tersedia):
        self.__judul = judul
        self.__harga_tiket = harga_tiket
        self.__kursi_tersedia = kursi_tersedia

    # Getter & Setter
    def get_judul(self):
        return self.__judul

    def get_harga_tiket(self):
        return self.__harga_tiket

    def get_kursi_tersedia(self):
        return self.__kursi_tersedia

    def set_kursi_tersedia(self, jumlah_baru):
        if jumlah_baru >= 0:
            self.__kursi_tersedia = jumlah_baru
        else:
            print("Jumlah kursi tidak boleh negatif!")

    def pesan_kursi(self, jumlah):
        if jumlah <= self.__kursi_tersedia:
            self.__kursi_tersedia -= jumlah
            return True
        else:
            print(f"Jumlah yang ingin dipesan melebihi kursi tersedia! "
                  f"(Sisa {self.__kursi_tersedia} kursi)")
            return False


# Class Utama: Penonton
class Penonton:
    def __init__(self, nama):
        self._nama = nama
        self._tiket_dipesan = []
        self._waktu_daftar = datetime.now()

    def get_nama(self):
        return self._nama

    def get_tiket_dipesan(self):
        return self._tiket_dipesan

    # Polymorphism: method ini akan dioverride oleh turunan
    def hitung_total_harga(self, harga, jumlah):
        return harga * jumlah  

    def pesan_tiket(self, film, jumlah):
        if film.pesan_kursi(jumlah):
            harga = film.get_harga_tiket()
            total = self.hitung_total_harga(harga, jumlah)
            waktu = datetime.now().strftime("%H:%M:%S")
            self._tiket_dipesan.append((film.get_judul(), jumlah, total, waktu))
            print(f"{self._nama} memesan {jumlah} tiket '{film.get_judul()}' "
                  f"(Total: Rp{total:,.0f}) pada {waktu}")

    def tampilkan_tiket(self):
        print(f"\n=== Tiket {self._nama} ===")
        if not self._tiket_dipesan:
            print("Belum ada tiket yang dipesan.")
            return
        total_semua = 0
        for judul, jumlah, total, waktu in self._tiket_dipesan:
            print(f"- {judul} x{jumlah} = Rp{total:,} (pada {waktu})")
            total_semua += total
        print(f"Total Bayar: Rp{total_semua:,}")


# Class Turunan: Member (Pewarisan + Polymorphism)
class Member(Penonton):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.__poin = poin
        self.__last_diskon = 0

    # Overriding method hitung_total_harga (Polymorphism)
    def hitung_total_harga(self, harga, jumlah):
        total = harga * jumlah
        if self.__poin > 100:
            diskon = total * 0.10  # Diskon 10%
        else:
            diskon = total * 0.05  # Diskon 5%

        total -= diskon
        self.__last_diskon = diskon
        return total

    def pesan_tiket(self, film, jumlah):
        if film.pesan_kursi(jumlah):
            harga = film.get_harga_tiket()
            total = self.hitung_total_harga(harga, jumlah)
            waktu = datetime.now().strftime("%H:%M:%S")
            self._tiket_dipesan.append((film.get_judul(), jumlah, total, waktu))

            print(f"{self._nama} mendapatkan diskon Rp{self.__last_diskon:,.0f}! "
                  f"Harga total menjadi Rp{total:,.0f}.")
            print(f"{self._nama} memesan {jumlah} tiket '{film.get_judul()}' "
                  f"pada {waktu}")

    def __str__(self):
        return f"Member: {self._nama} (Poin: {self.__poin})"


# Class Turunan: NonMember
class NonMember(Penonton):
    def hitung_total_harga(self, harga, jumlah):
        return harga * jumlah

    def __str__(self):
        return f"NonMember: {self._nama}"


# Demonstrasi Program
def main():
    # Buat film
    film1 = Film("Avengers: Endgame", 50000, 10)
    film2 = Film("Frozen 2", 40000, 6)

    # Buat penonton
    p1 = Member("Adit", 120)   
    p2 = Member("Budi", 80)   
    p3 = NonMember("Citra")   
    p4 = NonMember("Jamal")

    # Pemesanan tiket
    p1.pesan_tiket(film1, 3)
    p2.pesan_tiket(film1, 2)
    p3.pesan_tiket(film2, 2)
    p4.pesan_tiket(film1, 1)

    # Tampilkan tiket
    p1.tampilkan_tiket()
    p2.tampilkan_tiket()
    p3.tampilkan_tiket()

    print("\n=== Sisa Kursi Film ===")
    for f in [film1, film2]:
        print(f"{f.get_judul()}: {f.get_kursi_tersedia()} kursi tersisa")



if __name__ == "__main__":
    main()
