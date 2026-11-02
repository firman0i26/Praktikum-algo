# 1. LIST (Berurutan, bisa diuubah / mutable)
hobi = ["Membaca","Koding","Berenang"]
print("List Hobi:", hobi)
print("Tipe:", type(hobi))

# 2. TUPLE (Berurutan, TIDAK bisa diubah / immutable)
koordinat = (-6.1751,106.8650)
print("Tuple Koordinat:", koordinat)
print("Tipe:", type(koordinat))

# 3. DICTIONARY (Pasangan key : Value)
mahasiswa = {
    "nama": "Firman",
    "nim": "261080200036",
    "ipk": 4.00
}
print("Dict Mahasiswa:", mahasiswa)
print("Nama mahasiswa:", mahasiswa ["nama"])
print("Tipe:", type(mahasiswa))

# 4. SET (Nilai unik, tidak berurutan, tidak ada duplikat)
angka_unik = {1,2,3,4,5}
print("Set Angka Unik(otomatis menghapus duplikat):", angka_unik)
print("Tipe:", type(angka_unik))
