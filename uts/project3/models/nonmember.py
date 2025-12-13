from .penonton import Penonton

class NonMember(Penonton):
    def hitung_total_harga(self, harga, jumlah):
        return harga * jumlah

    def __str__(self):
        return f"NonMember: {self._nama}"
