# Kelas dasar
class HewanLiar:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    def makan(self):
        print(f"{self.nama} sedang makan.")
# Kelas turunan Harimau
class Harimau(HewanLiar):
    def mengaum(self):
        print(f"{self.nama} mengaum.")
# Kelas turunan Kucing
class Kucing(HewanLiar):
    def mengeong(self):
        print(f"{self.nama} mengeong.")
# Contoh penggunaan kelas di atas
harimau = Harimau("Rial", 5)
kucing = Kucing("Rial", 2)
harimau.makan()
harimau.mengaum()


