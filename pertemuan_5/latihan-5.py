class Notifikasi: 
    def kirim(self,pesan):
        raise NotImplementedError("Subclass harus mengimplementasikan method ini!")

class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")

class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")

class PushNotif(Notifikasi):
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")

daftar_notifikasi = [Email(), SMS(), PushNotif()]
pesan = "Diskon Spesial hanya untuk Anda!"

for notif in daftar_notifikasi:
    notif.kirim(pesan)

