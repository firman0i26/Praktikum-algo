import time

# 3. catatan waktu mulai
waktu_mulai = time.perf_counter()

#--- KODE YANG INGIN DIUKUR ---
# Contoh: Proses Perulangan hingga 10 juta kali
total = 0
for i in range(10_000_000) :
    total += i
    #print(i)
#------------------

# catat waktu selesai
waktu_selesai = time.perf_counter()

#hitung selesai waktu
lama_eksekusi = waktu_selesai - waktu_mulai

print(f"Hasil perhitungan:{total}")
print(f"Lama waktu eksekusi:{lama_eksekusi:.6f}detik")