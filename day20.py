# Meminta pengguna untuk memasukkan bilangan bulat pertama
bilangan_pertama = int(input("Masukkan bilangan bulat pertama: "))
# Meminta pengguna untuk memasukkan bilangan bulat kedua
bilangan_kedua = int(input("Masukkan bilangan bulat kedua: "))
# Melakukan operasi penjumlahan
penjumlahan = bilangan_pertama + bilangan_kedua
print("Hasil penjumlahan:", penjumlahan)
# Melakukan operasi pengurangan
pengurangan = bilangan_pertama - bilangan_kedua
print("Hasil pengurangan:", pengurangan)
# Melakukan operasi perkalian
perkalian = bilangan_pertama * bilangan_kedua
print("Hasil perkalian:", perkalian)
# Melakukan operasi pembagian
# Menghindari pembagian dengan nol
if bilangan_kedua != 0:
    pembagian = bilangan_pertama / bilangan_kedua
    print("Hasil pembagian:", pembagian)
else:
    print("Pembagian dengan nol tidak diperbolehkan")
