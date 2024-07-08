def pencarian_linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Contoh penggunaan
arr = [2, 3, 4, 10, 40]
x = 10

hasil = pencarian_linear(arr, x)
if hasil != -1:
    print(f"Elemen ditemukan pada indeks {hasil}")
else:
    print("Elemen tidak ditemukan dalam array")
