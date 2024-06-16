# Membuat dictionary
buah = {"apel": 10, "pisang": 15}

# Mengakses elemen dictionary 
print(buah["apel"]) # Output: 10

# Menambahkan elemen baru 
buah["jeruk"] = 20

# Menghapus elemen
del buah["apel"]

print(buah) # Output: {'pisang': 15, 'jeruk': 20}

# Loop untuk mengakses key dan value
for kunci, nilai in buah.items():
    print(kunci, nilai)
