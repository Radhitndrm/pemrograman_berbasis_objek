
from datetime import datetime

class Penonton:
    def __init__(self, nama):
        self._nama = nama
        self._tiket_dipesan = []
        self._waktu_daftar = datetime.now()

    def get_nama(self):
        return self._nama

    def get_tiket_dipesan(self):
        return self._tiket_dipesan

    def hitung_total_harga(self, harga, jumlah):
        return harga * jumlah

    def pesan_tiket(self, film, jumlah):
        if film.pesan_kursi(jumlah):
            harga = film.get_harga_tiket()
            total = self.hitung_total_harga(harga, jumlah)
            waktu = datetime.now().strftime("%H:%M:%S")
            self._tiket_dipesan.append((film.get_judul(), jumlah, total, waktu))
            print(f"{self._nama} memesan {jumlah} tiket '{film.get_judul()}' (Total: Rp{total:,.0f}) pada {waktu}")

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
