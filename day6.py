phone_book = {}
for i in range(1, 6):
    nama = input(f"Masukkan nama teman ke-{i}: ")
    no_hp = input(f"Masukkan nomor telepon {nama}: ")
    phone_book[nama] = no_hp

print("\nPhone Book:")
for i, (nama, no_hp) in enumerate(phone_book.items(), 1):
    print(f"{i}. {nama} = {no_hp}")
