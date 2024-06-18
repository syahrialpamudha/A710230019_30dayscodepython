def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Penggunaan untuk persegi
sisi_persegi = float(input("Masukkan panjang sisi persegi: ")) 
luas_persegi, keliling_persegi = hitung_persegi(sisi_persegi)
print(f"Luas persegi: {luas_persegi}")
print(f"Keliling persegi: {keliling_persegi}")

# Penggunaan untuk persegi panjang
panjang_pp = float(input("Masukkan panjang persegi panjang: ")) 
lebar_pp = float(input("Masukkan lebar persegi panjang: "))
luas_pp, keliling_pp = hitung_persegi_panjang(panjang_pp, lebar_pp)
print(f"Luas persegi panjang: {luas_pp}")
print(f"Keliling persegi panjang: {keliling_pp}")
