
class Film:
    def __init__(self, judul, harga_tiket, kursi_tersedia):
        self.__judul = judul
        self.__harga_tiket = harga_tiket
        self.__kursi_tersedia = kursi_tersedia

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
            print(f"Jumlah yang ingin dipesan melebihi kursi tersedia! (Sisa {self.__kursi_tersedia} kursi)")
            return False
