def hitung_bahan_bakar(jarak_tempuh, efisiensi_bahan_bakar):
    return jarak_tempuh / efisiensi_bahan_bakar

def main():
    print("Program Menghitung Konsumsi Bahan Bakar Mobil")
    
    # Meminta input dari pengguna
    jarak_tempuh = float(input("Masukkan jarak tempuh (dalam km): "))
    efisiensi_bahan_bakar = float(input("Masukkan efisiensi bahan bakar mobil (dalam km/liter): "))
    
    # Menghitung konsumsi bahan bakar
    bahan_bakar_diperlukan = hitung_bahan_bakar(jarak_tempuh, efisiensi_bahan_bakar)
    
    # Menampilkan hasil
    print(f"Bahan bakar yang diperlukan untuk menempuh jarak {jarak_tempuh} km adalah {bahan_bakar_diperlukan:.2f} liter.")

if __name__ == "__main__":
    main()
