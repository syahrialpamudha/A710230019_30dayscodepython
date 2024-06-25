# Fungsi untuk menghitung akar pangkat 3
def akar_pangkat_tiga(angka):
    return angka ** (1/3)
# Angka yang akan dihitung akar pangkat 3-nya
angka = 27
# Menghitung akar pangkat 3 dari angka
hasil = akar_pangkat_tiga(angka)
# Menyimpan hasil ke dalam variabel
angka_dan_hasil = {
    "angka": angka,
    "hasil_akar_pangkat_tiga": hasil
}
# Menampilkan hasil
print(f"Angka: {angka_dan_hasil['angka']}, Akar Pangkat 3: {angka_dan_hasil['hasil_akar_pangkat_tiga']}")
