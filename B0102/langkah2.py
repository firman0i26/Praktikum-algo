# 1.DEKLARASI DATA DIRI MAHASISWA
nim = "2610080200036"
nama_mahasiswa = "Firman Abdika"
semester = 1
is_aktif = True #status registrasi ulang

#2. Data nilai mentah (simulasi input dari form web/database)
# Catatan:Input dari form seringkali terbaca sebagai string
str_nilai_algoritma = "85.5"
str_nilai_basisdata = "78.0"
str_nilai_pemograman_web = "90.2"
sks_per_matkul = 3 # Integer

# 3. Konversi tipe data (type casting)
nilai_algo = float(str_nilai_algoritma)
nilai_bd =  float(str_nilai_basisdata)
nilai_web = float(str_nilai_pemograman_web)

# 4. Kalkulasi menggunakan vaeriabel
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai/jumlah_matkul
total_sks_diambil = jumlah_matkul*sks_per_matkul

# Penentuan status kelulusan semester (boolean)
# Lulus jika rata-rata >= 75.0 dan status mahasiswa aktif
is_lulus_semester = (rata_rata_nilai>= 75.0)  and is_aktif

print("\n--HASIL EVALUASI AWAL--")
print("Total Nilai :", total_nilai)
print("Rata-Rata Nilai :", round(rata_rata_nilai))
print("TOtal sks :", total_sks_diambil)
print("Status Lulus :", is_lulus_semester)