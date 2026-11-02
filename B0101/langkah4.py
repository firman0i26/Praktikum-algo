# 1. konversi dari String Ke Integer
str_angka = "100"
int_angka = int(str_angka)
print("Hasil penjumlahan (100+50):", int_angka +50)

# 2. konversei dari float ke integer (Angka dibelakang koma dihilangkan)
ipk_float = 4.00
ipk_int = int(ipk_float)
print("Float ke int:", ipk_int)

# 3.kkonversi dari integer ke string
tahun = 2024
pesan = "Tahun saat ini:" + str(tahun)
print(pesan)

# 4. konversi dari list ke set(Menghapus elemen duplikat)
daftar_buah = ["Apel","Jeruk","Apel","Pisang","Jeruk"]
buah_unik = set(daftar_buah)
print("Buah Unik:", buah_unik)