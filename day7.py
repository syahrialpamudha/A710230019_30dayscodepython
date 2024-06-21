class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.pekerja = []

    def tambah_pekerja(self, nama):
        self.pekerja.append(nama)

    def jumlah_pekerja(self):
        return len(self.pekerja)

    def tampilkan_pekerja(self):
        print(", ".join(self.pekerja))


# Contoh penggunaan
perusahaan = Perusahaan("PT Kartasura Raceway")

perusahaan.tambah_pekerja("Syahrial")
perusahaan.tambah_pekerja("Pamudha")
perusahaan.tambah_pekerja("Wardhana")

print(f"Jumlah pekerja: {perusahaan.jumlah_pekerja()}")

perusahaan.tampilkan_pekerja()
