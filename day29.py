# Daftar harga lada di pasar selama satu minggu
harga_lada = [50000, 52000, 51000, 49500, 50500, 53000, 51500]

# Menghitung rata-rata harga lada
rata_rata_harga = sum(harga_lada) / len(harga_lada)

# Menampilkan hasil
print(f"Harga rata-rata lada di pasar selama satu minggu adalah Rp {rata_rata_harga:.2f}")

# Menampilkan harga lada per hari
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

for i in range(len(hari)):
    print(f"Harga lada pada hari {hari[i]} adalah Rp {harga_lada[i]:.2f}")
