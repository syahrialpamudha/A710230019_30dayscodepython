def main():
    # Membuat daftar untuk menyiapkan jenis pakaian
    pakaian_list = []
    # Meminta pengguna untuk memasukkan jenis pakaian hingga pengguna berhenti
    while True:
        jenis_pakaian = input("Masukkan jenis pakaian (atau ketik 'selesai' untuk mengakhiri): ")
        if jenis_pakaian.lower() == 'selesai':
            break
        pakaian_list.append(jenis_pakaian)
    # Menampilkan daftar pakaian yang dimasukkan
    print("Daftar pakaian yang dimasukkan:")
    for pakaian in pakaian_list:
        print(f"- {pakaian}")
if __name__ == "__main__":
    main()


