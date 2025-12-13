class Bentuk:
    def gambar(self): 
        raise NotImplementedError("Subclass harus mengimplementasikan method ini!")

class Persegi(Bentuk):
    def gambar(self):
        print("Menggambar Persegi : [][][][]" )

class Lingkaran(Bentuk):
    def gambar(self):
        print("Menggambar Lingkaran: 000000")

daftar_bentuk = [Persegi(), Lingkaran(), Persegi(), Lingkaran()]

print("--- Memanggil method yang sama pada objek yang berbeda ---")
for bentuk in daftar_bentuk:
    bentuk.gambar()

class Segitiga(Bentuk):
    def gambar(self):
        print("Menggambar Segitiga: /\\")

class Teks:
    def gambar(self):
        print("Menulis Teks: 'Hello, Polymorphism!'")

def render_objek(objek_untuk_digambar):
    print("Mencoba me-render objek...")
    objek_untuk_digambar.gambar()

persegi = Persegi()
lingkaran = Lingkaran() 
segitiga = Segitiga()
teks_biasa= Teks()

print("\n--- Menggunakan fungsi polimorfik ---")
render_objek(persegi)
render_objek(lingkaran)
render_objek(segitiga)

print("\n --- Demonstrasi Duck Typing ---")
render_objek(teks_biasa)
