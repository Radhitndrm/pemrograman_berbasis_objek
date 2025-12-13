
import os
from datetime import datetime
from math import ceil

class Laporan:
    def __init__(self, nama_file="laporan.txt"):
        self.nama_file = nama_file

    def simpan_laporan(self, daftar_penonton):
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open(self.nama_file, "w", encoding="utf-8") as f:
            f.write(f"LAPORAN PEMESANAN TIKET\nTanggal: {waktu}\n\n")

            for p in daftar_penonton:
                f.write(f"Nama: {p.get_nama()}\n")
                tiket = p.get_tiket_dipesan()
                if not tiket:
                    f.write("  Tidak ada tiket yang dipesan.\n\n")
                    continue
                total = 0
                for judul, jumlah, harga, waktu in tiket:
                    f.write(f"  - {judul} x{jumlah} = Rp{ceil(harga):,} (pada {waktu})\n")
                    total += harga
                f.write(f"  Total: Rp{ceil(total):,}\n\n")

        print(f"\n✅ Laporan berhasil disimpan ke '{os.path.abspath(self.nama_file)}'")
