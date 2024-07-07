class Pengurus:
    def __init__(self, nama, jabatan, tahun_menjabat):
        self.nama = nama
        self.jabatan = jabatan
        self.tahun_menjabat = tahun_menjabat
class Sekolah:
    def __init__(self, nama_sekolah):
        self.nama_sekolah = nama_sekolah
        self.daftar_pengurus = []
    def tambah_pengurus(self, pengurus):
        self.daftar_pengurus.append(pengurus)
    def tampilkan_pengurus(self):
        print(f"Nama Sekolah: {self.nama_sekolah}")
        print("Daftar Pengurus:")
        for pengurus in self.daftar_pengurus:
            print(f"- Nama: {pengurus.nama}, Jabatan: {pengurus.jabatan}, Tahun Menjabat: {pengurus.tahun_menjabat} tahun")

# Membuat objek Pengurus dengan nama-nama guru dan jabatan masing-masing
pengurus1 = Pengurus("Pak Adi", "Kepala Sekolah", 5)
pengurus2 = Pengurus("Pak Eko", "Wakil Kepala Sekolah", 3)
pengurus3 = Pengurus("Bu Erna", "Bendahara", 4)
pengurus4 = Pengurus("Bu Retno", "Sekretaris", 2)

# Membuat objek Sekolah dengan nama SMA N 1 Jatisrono
sekolah = Sekolah("SMA N 1 Jatisrono")

# Menambahkan pengurus ke dalam daftar pengurus sekolah
sekolah.tambah_pengurus(pengurus1)
sekolah.tambah_pengurus(pengurus2)
sekolah.tambah_pengurus(pengurus3)
sekolah.tambah_pengurus(pengurus4)

# Menampilkan informasi sekolah dan daftar pengurus
sekolah.tampilkan_pengurus()
