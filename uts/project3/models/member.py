
from datetime import datetime
from .penonton import Penonton

class Member(Penonton):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.__poin = poin
        self.__last_diskon = 0

    def hitung_total_harga(self, harga, jumlah):
        total = harga * jumlah
        if self.__poin > 100:
            diskon = total * 0.10
        else:
            diskon = total * 0.05

        total -= diskon
        self.__last_diskon = diskon
        return total

    def pesan_tiket(self, film, jumlah):
        if film.pesan_kursi(jumlah):
            harga = film.get_harga_tiket()
            total = self.hitung_total_harga(harga, jumlah)
            waktu = datetime.now().strftime("%H:%M:%S")
            self._tiket_dipesan.append((film.get_judul(), jumlah, total, waktu))
            print(f"{self._nama} mendapatkan diskon Rp{self.__last_diskon:,.0f}! Harga total: Rp{total:,.0f}")
            print(f"{self._nama} memesan {jumlah} tiket '{film.get_judul()}' pada {waktu}")

    def __str__(self):
        return f"Member: {self._nama} (Poin: {self.__poin})"
