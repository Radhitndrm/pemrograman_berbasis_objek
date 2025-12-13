

from .karakter import Karakter

class Musuh(Karakter):
    def __init__(self, nama, hp, serangan):
        super().__init__(nama, hp, serangan)

    def serang(self, target):
        print(f"{self.get_nama()} menyerang {target.get_nama()} dengan ganas!")
        target.set_hp(target.get_hp() - self.get_serangan())
        print(f"{target.get_nama()} kehilangan {self.get_serangan()} HP! Sisa HP: {target.get_hp()}")
