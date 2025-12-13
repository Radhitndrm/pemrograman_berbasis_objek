
# Project 1: Sistem Bioskop

class Film:
    def __init__(self, judul, harga_tiket, kursi_tersedia):
        self.__judul = judul    # atribut privat
        self.__harga_tiket = harga_tiket
        self.__kursi_tersedia = kursi_tersedia

    # Getter dan Setter
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
            print(f"Kursi tidak cukup! Tersisa {self.__kursi_tersedia}.")
            return False


class Penonton:
    def __init__(self, nama):
        self.__nama = nama
        self.__tiket_dipesan = []

    def get_nama(self):
        return self.__nama

    def get_tiket_dipesan(self):
        return self.__tiket_dipesan

    def pesan_tiket(self, film, jumlah):
        if film.pesan_kursi(jumlah):
            total = film.get_harga_tiket() * jumlah
            self.__tiket_dipesan.append((film.get_judul(), jumlah, total))
            print(f"{self.__nama} berhasil memesan {jumlah} tiket '{film.get_judul()}' (Total: Rp{total:,})")

    def tampilkan_tiket(self):
        print(f"\n=== Tiket {self.__nama} ===")
        if not self.__tiket_dipesan:
            print("Belum ada tiket yang dipesan.")
            return
        total_semua = 0
        for judul, jumlah, total in self.__tiket_dipesan:
            print(f"- {judul} x{jumlah} = Rp{total:,}")
            total_semua += total
        print(f"Total Bayar: Rp{total_semua:,}")


# Demonstrasi Program
def main():
    # Buat objek film
    film1 = Film("Avengers: Endgame", 50000, 10)
    film2 = Film("Frozen 2", 40000, 5)

    # Buat objek penonton
    penonton1 = Penonton("Adit")
    penonton2 = Penonton("Budi")
    penonton3 = Penonton("Citra")

    # Pemesanan tiket
    penonton1.pesan_tiket(film1, 3)
    penonton2.pesan_tiket(film1, 5)
    penonton3.pesan_tiket(film1, 3)  # tidak cukup kursi
    penonton3.pesan_tiket(film2, 2)

    # Tampilkan tiket masing-masing penonton
    penonton1.tampilkan_tiket()
    penonton2.tampilkan_tiket()
    penonton3.tampilkan_tiket()

    # Cek sisa kursi
    print("\n=== Sisa Kursi Film ===")
    for f in [film1, film2]:
        print(f"{f.get_judul()}: {f.get_kursi_tersedia()} kursi tersisa")

if __name__ == "__main__":
    main()
