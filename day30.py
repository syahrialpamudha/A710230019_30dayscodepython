def bagi(angka1, angka2):
    try:
        hasil = angka1 / angka2
    except ZeroDivisionError:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    except TypeError:
        return "Error: Input harus berupa angka."
    else:
        return f"Hasil: {hasil}"
    finally:
        print("Eksekusi blok try-except selesai.")

# Contoh penggunaan
angka1 = 10
angka2 = 0

print(bagi(angka1, angka2))  # Akan menghasilkan error karena pembagian dengan nol

angka1 = 10
angka2 = 2

print(bagi(angka1, angka2))  # Akan menghasilkan hasil pembagian yang benar

angka1 = 10
angka2 = "a"

print(bagi(angka1, angka2))  # Akan menghasilkan error karena input bukan angka
