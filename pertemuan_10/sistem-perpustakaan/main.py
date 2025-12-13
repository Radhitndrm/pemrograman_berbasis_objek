
from buku import Buku
from pustaka import Pustaka
from anggota import Anggota

buku1 = Buku("Harry Potter", "J.K. Rowling")
buku2 = Buku("The Hobbit", "J.R.R. Tolkien")

pustaka = Pustaka()
pustaka.tambah_buku(buku1)
pustaka.tambah_buku(buku2)

anggota1 = Anggota("Andi")

anggota1.pinjam_buku(buku1)
anggota1.pinjam_buku(buku2)

pustaka.tampilkan_koleksi()

anggota1.kembalikan_buku(buku1)

print("\nStatus Koleksi Setelah Pengembalian:")
pustaka.tampilkan_koleksi()
