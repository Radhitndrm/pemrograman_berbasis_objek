from entities.pemain import Pemain
from entities.musuh import Musuh
from items.item import Item

pemain1 = Pemain("Arka", hp=100, serangan=20)
musuh1 = Musuh("Goblin", hp=60, serangan=10)

ramuan = Item("Ramuan Penyembuh", efek_hp=30)
pedang = Item("Pedang Api", efek_serangan=10)

pemain1.ambil_item(ramuan)
pemain1.ambil_item(pedang)

pemain1.gunakan_item(pedang)
pemain1.serang(musuh1)

musuh1.serang(pemain1)

pemain1.gunakan_item(ramuan)
pemain1.serang(musuh1)

print("\n--- Status Akhir ---")
print(f"{pemain1.get_nama()}: {pemain1.get_hp()} HP")
print(f"{musuh1.get_nama()}: {musuh1.get_hp()} HP")
