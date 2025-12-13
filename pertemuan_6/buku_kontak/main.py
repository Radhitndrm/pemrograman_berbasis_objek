from models.kontak import Kontak

if __name__ == "__main__":
    daftar_kontak = []

    kontak1 = Kontak("Syahrul", "081234567890")
    kontak2 = Kontak("Babloi", "089876543210")
    kontak3 = Kontak("Jarpis", "087712345678")

    daftar_kontak.extend([kontak1, kontak2, kontak3])

    print("--- Daftar Kontak ---")
    for kontak in daftar_kontak:
        kontak.tampilkan_info()
