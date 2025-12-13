
from models.film import Film
from models.member import Member
from models.nonmember import NonMember
from utils.laporan import Laporan
from utils.log_aktivitas import catat_aktivitas

def main():
    # Buat film
    film1 = Film("Avengers: Endgame", 50000, 10)
    film2 = Film("Frozen 2", 40000, 6)

    # Buat penonton
    p1 = Member("Adit", 120)
    p2 = Member("Budi", 80)
    p3 = NonMember("Citra")
    p4 = NonMember("Jamal")

    catat_aktivitas("Program dimulai - simulasi pemesanan tiket")

    # Pemesanan tiket
    p1.pesan_tiket(film1, 3); catat_aktivitas(f"{p1.get_nama()} memesan tiket Avengers")
    p2.pesan_tiket(film1, 2); catat_aktivitas(f"{p2.get_nama()} memesan tiket Avengers")
    p3.pesan_tiket(film2, 2); catat_aktivitas(f"{p3.get_nama()} memesan tiket Frozen 2")
    p4.pesan_tiket(film1, 1); catat_aktivitas(f"{p4.get_nama()} memesan tiket Avengers")

    # Tampilkan tiket
    for p in [p1, p2, p3, p4]:
        p.tampilkan_tiket()

    # Simpan laporan
    laporan = Laporan()
    laporan.simpan_laporan([p1, p2, p3, p4])

    catat_aktivitas("Program selesai - laporan disimpan")

if __name__ == "__main__":
    main()
