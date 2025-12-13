
class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def pinjam_buku(self, buku):
        if not buku.dipinjam:
            buku.dipinjam = True
            self.daftar_buku.append(buku)
            print(f"{self.nama} meminjam buku '{buku.judul}'")
        else:
            print(f"Buku '{buku.judul}' sedang dipinjam orang lain")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_buku:
            buku.dipinjam = False
            self.daftar_buku.remove(buku)
            print(f"{self.nama} mengembalikan buku '{buku.judul}'")
        else:
            print(f"{self.nama} tidak meminjam buku '{buku.judul}'")
