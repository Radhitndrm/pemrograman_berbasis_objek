class Buku:
    def __init__(self, input_judul, input_penulis, input_tahun_terbit):
        self.judul = input_judul
        self.penulis = input_penulis
        self.tahun_terbit = input_tahun_terbit
        self.status_pinjam = False

    def tampilkan_info(self):
        status = "Dipinjam" if self.status_pinjam else "Tersedia"

        print(f"Judul        : {self.judul}")
        print(f"Penulis      : {self.penulis}")
        print(f"Tahun Terbit : {self.tahun_terbit}")
        print(f"Status       : {status}")
        print("-" * 40)


    def pinjam_buku(self):
        if not self.status_pinjam :
             self.status_pinjam = True
             print(f"Buku '{self.judul}' telah dipinjam.")
        else : 
            print(f"Buku '{self.judul}' sedang tidak tersedia (sedang dipinjam)")
        
    def kembalikan_buku(self): 
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"Buku '{self.judul}' telah dikembalikan ")
        else :
            print(f"Buku '{self.judul}' memang sudah tersedia")


buku1 = Buku("Crime & Punishment", "Fyodor Dostoyevsky", 1866)
buku2 = Buku("1984", "George Orwell", 1949)

print("\n--- Informasi Buku ---")
buku1.tampilkan_info()
buku2.tampilkan_info()

print("\n--- Buku yang dipinjam ---")
buku1.pinjam_buku()
buku1.tampilkan_info()

print("\n--- Buku yang dikembalikan ---")
buku1.kembalikan_buku()
buku1.tampilkan_info()

