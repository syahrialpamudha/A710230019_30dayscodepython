import datetime

def get_hari_libur_nasional(tahun):
    hari_libur = [(1, 1), (4, 21), (5, 1), (8, 17), (12, 25)]  # Tanggal libur tetap
    return [datetime.date(tahun, bulan, hari) for bulan, hari in hari_libur]

def hitung_tanggal_merah(tahun_awal, tahun_akhir):
    return sum(len(get_hari_libur_nasional(tahun)) for tahun in range(tahun_awal, tahun_akhir + 1))

tahun_awal = int(input("Masukkan tahun awal: "))
tahun_akhir = int(input("Masukkan tahun akhir: "))
total_tanggal_merah = hitung_tanggal_merah(tahun_awal, tahun_akhir)
print(f"Total tanggal merah dari tahun {tahun_awal} hingga {tahun_akhir} adalah {total_tanggal_merah}")
