import calendar

def cetak_kalender(tahun, bulan):
    # Membuat objek kalender
    kalender = calendar.TextCalendar(calendar.SUNDAY)
    
    # Menampilkan kalender untuk bulan dan tahun yang diberikan
    kalender_str = kalender.formatmonth(tahun, bulan)
    print(kalender_str)

def main():
    # Meminta input dari pengguna untuk tahun dan bulan
    tahun = int(input("Masukkan tahun (contoh, 2024): "))
    bulan = int(input("Masukkan bulan (1-12): "))
    
    # Memastikan input bulan valid
    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid. Masukkan angka antara 1 dan 12.")
        return
    
    # Menampilkan kalender
    cetak_kalender(tahun, bulan)

if __name__ == "__main__":
    main()
