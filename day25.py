class Baterai:
    def __init__(self):
        self.level = 100
        self.mengisi = False

    def gunakan(self, jumlah):
        self.level = max(0, self.level - jumlah)
        print(f"Level baterai: {self.level}%")

    def isi(self, jumlah):
        self.level = min(100, self.level + jumlah)
        print(f"Level baterai: {self.level}%")

    def mulai_isi(self):
        self.mengisi = True
        print("Pengisian dimulai.")

    def berhenti_isi(self):
        self.mengisi = False
        print("Pengisian dihentikan.")

# Contoh penggunaan
baterai = Baterai()
baterai.gunakan(20)
baterai.mulai_isi()
baterai.isi(15)
baterai.berhenti_isi()
