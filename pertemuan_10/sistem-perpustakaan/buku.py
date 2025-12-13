
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False

    def tampilkan_info(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"Buku: {self.judul}, Penulis: {self.penulis}, Status: {status}"
