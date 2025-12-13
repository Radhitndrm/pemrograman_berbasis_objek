

class Item:
    def __init__(self, nama, efek_hp=0, efek_serangan=0):
        self.nama = nama
        self.efek_hp = efek_hp
        self.efek_serangan = efek_serangan

    def gunakan(self, pemain):
        pemain.set_hp(pemain.get_hp() + self.efek_hp)
        pemain.set_serangan(pemain.get_serangan() + self.efek_serangan)
        print(f"{pemain.get_nama()} menggunakan {self.nama}! (+{self.efek_hp} HP, +{self.efek_serangan} Serangan)")
