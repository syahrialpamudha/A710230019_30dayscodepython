class Tiket:
    def __init__(self, harga_per_tiket):
        self.harga_per_tiket = harga_per_tiket

    def hitung_harga(self, jumlah):
        return self.harga_per_tiket * jumlah

def main():
    harga_tiket = {'biasa': 50000, 'vip': 100000, 'gold': 150000}
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket in harga_tiket:
        tiket = Tiket(harga_tiket[jenis_tiket])
        total_harga = tiket.hitung_harga(jumlah_tiket)
        print(f"Total Harga Tiket: Rp{total_harga}")
    else:
        print("Jenis tiket tidak valid.")

if __name__ == "__main__":
    main()
