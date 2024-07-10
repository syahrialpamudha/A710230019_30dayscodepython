class Jam:
    def __init__(self, jam=0, menit=0, detik=0):
        self.set_waktu(jam, menit, detik)

    def set_waktu(self, jam, menit, detik):
        if not (0 <= jam < 24 and 0 <= menit < 60 and 0 <= detik < 60):
            raise ValueError("Waktu tidak valid.")
        self.jam, self.menit, self.detik = jam, menit, detik

    def tambah_detik(self):
        self.detik = (self.detik + 1) % 60
        if self.detik == 0:
            self.menit = (self.menit + 1) % 60
            if self.menit == 0:
                self.jam = (self.jam + 1) % 24

    def tampilkan_waktu(self):
        return f"{self.jam:02}:{self.menit:02}:{self.detik:02}"

# Contoh penggunaan
jam_sekarang = Jam(23, 59, 50)
print("Waktu sekarang:", jam_sekarang.tampilkan_waktu())

# Tambahkan beberapa detik
for _ in range(15):
    jam_sekarang.tambah_detik()
    print("Waktu sekarang:", jam_sekarang.tampilkan_waktu())
