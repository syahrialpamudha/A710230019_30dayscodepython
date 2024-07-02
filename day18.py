def kalkulator():
    num1 = float(input("Bilangan pertama: "))
    operasi = input("Pilih operasi (+, -, *, /): ")
    num2 = float(input("Bilangan kedua: "))
    if operasi == '+':
        hasil = num1 + num2
    elif operasi == '-':
        hasil = num1 - num2
    elif operasi == '*':
        hasil = num1 * num2
    elif operasi == '/':
        hasil = "Error! Tidak bisa membagi dengan nol." if num2 == 0 else num1 / num2
    else:
        return "Operasi tidak valid."
    return f"Hasil: {num1} {operasi} {num2} = {hasil}"
print(kalkulator())
