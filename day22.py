class Karyawan:
    def __init__(self, nama, id, gaji_dasar, bonus=0, jam_kerja=0, tarif_per_jam=0):
        self.nama = nama
        self.id = id
        self.gaji_dasar = gaji_dasar
        self.bonus = bonus
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam

    def hitung_gaji(self):
        return self.gaji_dasar + self.bonus + (self.jam_kerja * self.tarif_per_jam)

    def __str__(self):
        return f"Karyawan [Nama: {self.nama}, ID: {self.id}, Gaji: {self.hitung_gaji()}]"

def main():
    # Membuat objek karyawan penuh waktu
    karyawan_penuh_waktu = Karyawan("Alice", 1, 5000000, bonus=1000000)
    print(karyawan_penuh_waktu)

    # Membuat objek karyawan paruh waktu
    karyawan_paruh_waktu = Karyawan("Bob", 2, 1000000, jam_kerja=50, tarif_per_jam=200000)
    print(karyawan_paruh_waktu)

if __name__ == "__main__":
    main()
