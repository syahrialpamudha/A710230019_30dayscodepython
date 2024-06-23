while True:
    user_input = input("Masukkan bilangan bulat: ")
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        angka = int(user_input)
        print(f"Hasil kuadrat dari {angka} adalah {angka ** 2}")
        break
    else:
        print("Input yang dimasukkan tidak valid! Silakan masukkan bilangan bulat.")
