class Sekolah:
    def __init__(self):
        self.siswa = 0
        self.guru = 0
    def tambah_siswa(self, jumlah=1):
        self.siswa += jumlah
    def tambah_guru(self, jumlah=1):
        self.guru += jumlah
    def total_siswa(self):
        return self.siswa
    def total_guru(self):
        return self.guru
    def total_orang(self):
        return self.siswa + self.guru

# Membuat objek Sekolah
sekolah = Sekolah()
# Menambahkan siswa dan guru
sekolah.tambah_siswa(2)  # Menambahkan 2 siswa
sekolah.tambah_guru(2)   # Menambahkan 2 guru
# Menghitung dan mencetak jumlah siswa dan guru
print(f"Total Siswa: {sekolah.total_siswa()}")
print(f"Total Guru: {sekolah.total_guru()}")
print(f"Total Orang (Siswa + Guru): {sekolah.total_orang()}")
