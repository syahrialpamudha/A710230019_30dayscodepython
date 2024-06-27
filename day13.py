def get_integer_input(prompt="Masukkan sebuah bilangan bulat: "):
    while True:
        user_input = input(prompt)
        try:
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Input yang dimasukkan tidak valid! Silakan masukkan bilangan bulat.")
def main():
    bilangan = get_integer_input()
    hasil_kuadrat = bilangan ** 2
    print(f"Hasil kuadrat dari {bilangan} adalah {hasil_kuadrat}")
if __name__ == "__main__":
    main()
