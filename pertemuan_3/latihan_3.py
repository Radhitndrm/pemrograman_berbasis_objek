
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji

    def get_nama(self):
        return self.__nama

    def get_id(self):
        return self.__id_karyawan

    def get_gaji(self):
        return self.__gaji

    def set_nama(self, nama_baru):
        if nama_baru.strip() == "":
            print("Error: Nama tidak boleh kosong.")
        else:
            self.__nama = nama_baru

    def set_gaji(self, gaji_baru):
        if isinstance(gaji_baru, (int, float)) and gaji_baru > 0:
            self.__gaji = gaji_baru
        else:
            print("Error: Gaji harus berupa angka positif.")

if __name__ == "__main__":
    karyawan1 = Karyawan("Yusuf Mizan", "K001", 5000000)

    print("Informasi Karyawan Awal:")
    print(f"Nama: {karyawan1.get_nama()}")
    print(f"ID: {karyawan1.get_id()}")
    print(f"Gaji: {karyawan1.get_gaji()}")

    print("\nMencoba ubah gaji menjadi -5000000:")
    karyawan1.set_gaji(-5000000)
    print(f"Gaji sekarang: {karyawan1.get_gaji()}")

    print("\nMencoba ubah nama menjadi string kosong:")
    karyawan1.set_nama("")
    print(f"Nama sekarang: {karyawan1.get_nama()}")

    print("\nMengubah gaji menjadi 6000000:")
    karyawan1.set_gaji(6000000)
    print(f"Gaji sekarang: {karyawan1.get_gaji()}")

    print("\nMengubah nama karyawaman menjadi Ronaldo :")
    karyawan1.set_nama("Ronaldo")
    print(f"Nama sekarang: {karyawan1.get_nama()}")

    print("\nInformasi Karyawan Setelah Update:")
    print(f"Nama: {karyawan1.get_nama()}")
    print(f"ID: {karyawan1.get_id()}")
    print(f"Gaji: {karyawan1.get_gaji()}")
