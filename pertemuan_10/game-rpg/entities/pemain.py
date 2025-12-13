

from .karakter import Karakter

class Pemain(Karakter):
    def __init__(self, nama, hp, serangan):
        super().__init__(nama, hp, serangan)
        self._inventory = []

    def ambil_item(self, item):
        self._inventory.append(item)
        print(f"{self.get_nama()} mengambil item: {item.nama}")

    def gunakan_item(self, item):
        if item in self._inventory:
            item.gunakan(self)
            self._inventory.remove(item)
        else:
            print("Item tidak ditemukan.")

    def serang(self, target):
        print(f"{self.get_nama()} menyerang {target.get_nama()}!")
        target.set_hp(target.get_hp() - self.get_serangan())
        print(f"{target.get_nama()} menerima {self.get_serangan()} damage. Sisa HP: {target.get_hp()}")
