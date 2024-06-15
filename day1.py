
# Fungsi untuk menghitung luas persegi panjang
def hitung_luas(panjang, lebar):
    return panjang * lebar
# Fungsi untuk menghitung keliling persegi panjang
def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Menghitung luas dan keliling
luas = hitung_luas(panjang, lebar)
keliling = hitung_keliling(panjang, lebar)

# Menampilkan hasil
print(f"Luas persegi panjang: {luas}")
print(f"Keliling persegi panjang: {keliling}")
