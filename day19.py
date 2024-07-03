from abc import ABC, abstractmethod
class Orang(ABC):
  def __init__(self, nama):
    self.nama = nama
  @abstractmethod
  def beraktivitas(self):
    pass
class Siswa(Orang):
  def beraktivitas(self):
    print(f"{self.nama} sedang belajar.")
class Guru(Orang):
  def beraktivitas(self):
    print(f"{self.nama} sedang mengajar.")
def lakukan_aktivitas(orang):
  orang.beraktivitas()
# Buat objek Siswa dan Guru
siswa = Siswa("rial")
guru = Guru("dana")
# Lakukan aktivitas Siswa dan Guru
lakukan_aktivitas(siswa)
lakukan_aktivitas(guru)
