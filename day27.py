def hitung_bensin(jarak_tempuh, efisiensi_bahan_bakar):
    """
    Fungsi untuk menghitung jumlah bensin yang diperlukan untuk menempuh jarak tertentu.
    
    Parameter:
    - jarak_tempuh (float): Jarak yang akan ditempuh dalam kilometer.
    - efisiensi_bahan_bakar (float): Efisiensi bahan bakar dalam kilometer per liter (km/l).
    
    Return:
    - (float): Jumlah bensin yang diperlukan dalam liter, atau None jika efisiensi bahan bakar tidak valid.
    """
    if efisiensi_bahan_bakar <= 0:
        return None
    
    bensin_diperlukan = jarak_tempuh / efisiensi_bahan_bakar
    return bensin_diperlukan

# Contoh penggunaan
jarak_tempuh = 150  # dalam kilometer
efisiensi_bahan_bakar = 30  # dalam kilometer per liter (km/l)

bensin_diperlukan = hitung_bensin(jarak_tempuh, efisiensi_bahan_bakar)
if bensin_diperlukan is None:
    print("Efisiensi bahan bakar harus lebih besar dari nol.")
else:
    print(f"Jumlah bensin yang diperlukan untuk menempuh {jarak_tempuh} km adalah {bensin_diperlukan:.2f} liter.")
