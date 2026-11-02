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

daftar_matkul = ["Algoritma dan Pemograman","Basis Data","Pemograman web"]

transkip_nilai = {
    "Algoritma dan Pemograman":4.0,   # Nilai A
    "Basis Data":3.0,                 # Nilai B
    "Pemograman Web":4.0              # Nilai A
}

# 6. Update variabel dinamis
# mahasiswa mengambil matkul  susulan
matkul_baru = "jaringan komputer"
nilai_matkul_baru ="88.0"
mutu_matkul_baru = 3.5

# A Tambahkan ke list
daftar_matkul.append(matkul_baru)

# B Tambahkan ke Dictionary
transkip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi variabel total dan rata-rata
nilai_jk = float(nilai_matkul_baru)
total_nilai = total_nilai * nilai_jk
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. hitung indeks pretasi kumulatif (ipk) dari Dictionary Mutu
total_bobot_mutu = sum(transkip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL--")
print("Daftar Matkul Terbaru:", daftar_matkul)
print("jumlah matkul total:", jumlah_matkul)
print("Rata-Rata Angka Baru:", round(rata_rata_terbaru ,2))
print("IPK Sementara (Skala 4):", round(ipk_sementara ,2))
