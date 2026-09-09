import random
import math

# =========================================================#
# FUNDAMENTAL DASAR#

# 0. VARIABLES AND LITERALS
# --- Multiple assignment
nama_anggota, id_anggota = "FERRY", 2595114023
print("Nama pasien:", nama_anggota)
print("ID pasien  :", id_anggota)

# --- Assign nilai sama ke beberapa variabel sekaligus
kuota_a = kuota_b = kuota_c = 3   # tiga pasien baru sama-sama dapat kuota default 3
print(f"kuota_a={kuota_a}, kuota_b={kuota_b}, kuota_c={kuota_c}")

# --- Konvensi "constant" (Python tidak punya true constant, ini cuma konvensi huruf besar)
MAKS_KUNJUNGAN_PER_PASIEN = 5
print("Batas maksimal kunjungan:", MAKS_KUNJUNGAN_PER_PASIEN)
# catatan realistis: MAKS_KUNJUNGAN_PER_PASIEN di atas SECARA TEKNIS masih bisa
# ditimpa/diubah nilainya di baris lain. Huruf besar cuma konvensi penanda
# "jangan diubah", Python tidak benar-benar menguncinya.

# --- Literals
literal_integer = 2595114023         # numeric literal (int)
literal_float = 4.7                   # numeric literal (float)
literal_underscore = 1_000_000        # underscore cuma pemisah biar gampang dibaca manusia
literal_string = 'Perpustakaan Kampus'  # string literal
literal_boolean = True                # boolean literal
literal_khusus = None                 # special literal, artinya "belum ada nilai"

print("Literal int (dengan underscore):", literal_underscore)
print("Literal string:", literal_string)
print("Literal None  :", literal_khusus)

# =========================================================#
# 1. TYPE CONVERSION

# --- 1.0 Implicit Type Conversion
jumlah_pasien = 120                  # int -> jumlah eksemplar buku
rata_rata_kunjungan_harian = 3.5      # float -> rata-rata buku dipinjam per hari

proyeksi_kunjungan = jumlah_pasien + rata_rata_kunjungan_harian
print("Nilai:", proyeksi_kunjungan)
print("Tipe Data:", type(proyeksi_kunjungan))
# Python otomatis mengubah int jadi float saat dijumlah dengan float

# --- 1.2 Explicit Type Conversion
id_scan = '015'            # simulasi hasil scan kartu anggota, selalu berupa string
nomor_transaksi = 41       # int

print("Tipe id_scan sebelum casting:", type(id_scan))
id_scan = int(id_scan)     # wajib di-cast dulu sebelum dipakai operasi numerik
print("Tipe id_scan sesudah casting:", type(id_scan))

kode_rekam = nomor_transaksi + id_scan
print("Kode gabungan:", kode_rekam)
print("Tipe kode_rekam:", type(kode_rekam))

# =========================================================#
# 2. BASIC INPUT & OUTPUT

nama_klinik = "Klinik Sehat Bersama"

# --- 2.0 print dasar
print("Selamat Datang!")
print(f"Anda berada di {nama_klinik}")

# --- 2.1 print dengan parameter end
print("Selamat Datang!", end=' ')
print(f"di {nama_klinik}")

# --- 2.2 print dengan parameter sep, literal, dan variabel
print("Tahun Operasional", 2026, "Tetap sehat!", sep='. ')

saldo_tagihan = -750          # literal negatif -> misal saldo lebih bayar denda (refund)
print(5)                     # contoh literal murni
print(saldo_tagihan)
print(nama_klinik)

# =========================================================#
# 3. OPERATORS

# --- 3.0 Arithmetic Operators
stok_obat = 10
obat_terpakai = 9
print('stok + terpakai  =', stok_obat + obat_terpakai)
print('stok - terpakai  =', stok_obat - obat_terpakai)
print('stok * terpakai  =', stok_obat * obat_terpakai)
print('stok / terpakai  =', stok_obat / obat_terpakai)
print('stok // terpakai =', stok_obat // obat_terpakai)
print('stok ** terpakai =', stok_obat ** obat_terpakai)

# --- 3.1 Comparison Operators
kuota_pasien = 16
jumlah_kunjungan = 11
print('kuota > dipinjam  is', kuota_pasien > jumlah_kunjungan)
print('kuota < dipinjam  is', kuota_pasien < jumlah_kunjungan)
print('kuota == dipinjam is', kuota_pasien == jumlah_kunjungan)
print('kuota != dipinjam is', kuota_pasien != jumlah_kunjungan)
print('kuota >= dipinjam is', kuota_pasien >= jumlah_kunjungan)
print('kuota <= dipinjam is', kuota_pasien <= jumlah_kunjungan)

# --- 3.2 Logical Operators
pasien_aktif = True
punya_tagihan = False
print('pasien_aktif and punya_tagihan is', pasien_aktif and punya_tagihan)
print('pasien_aktif or punya_tagihan is', pasien_aktif or punya_tagihan)
print('not pasien_aktif is', not pasien_aktif)

# --- 3.3 Identity Operators
id1 = 5
id2 = 5
judul1 = 'Jadwal Dokter'
judul2 = 'Jadwal Dokter'
daftar1 = ['Umum', 'Anak']
daftar2 = ['Umum', 'Anak']
print(id1 is not id2)
print(judul1 is judul2)
print(daftar1 is daftar2)     # False -> dua list beda objek walau isinya sama

# --- 3.4 Membership Operators
judul_buku = 'Kartu Pasien'
kategori = {1: 'Umum', 2: 'Spesialis'}
print('B' in judul_buku)
print('Manusia' not in judul_buku)
print(1 in kategori)
print('Umum' in kategori)    # False -> 'in' pada dict mengecek KEY, bukan value

# =========================================================#
#FLOW CONTROL#
# 0. BOOLEANS & BOOLEAN EXPRESSIONS

# --- Nilai bool langsung ---
pasien_aktif = True
print("Status anggota aktif:", pasien_aktif, "->", type(pasien_aktif))

# --- Hasil perbandingan otomatis menghasilkan bool
stok_buku = 0
print("stok_buku > 0 menghasilkan:", stok_buku > 0)

# --- fungsi bool() dan konsep truthy / falsy
# Aturan pentingnya: 0, string kosong '', list kosong [], dan None dianggap False.
# Selain itu (angka bukan nol, string berisi teks, list berisi data) dianggap True.
print("bool(0)          :", bool(0))            # falsy
print("bool(1)          :", bool(1))            # truthy
print("bool('')         :", bool(''))           # falsy, string kosong
print("bool('Obat')     :", bool('Obat'))       # truthy, string berisi teks
print("bool([])         :", bool([]))           # falsy, list kosong
print("bool(['Obat A']) :", bool(['Obat A']))   # truthy, list berisi data

# --- Kenapa ini penting: dipakai buat nyingkat pengecekan
daftar_resep = []
if daftar_resep:
    print("Pasien masih memiliki resep aktif.")
else:
    print("Tidak ada resep aktif.")
# baris di atas SAMA HASILNYA dengan "if len(daftar_resep) > 0:", tapi lebih ringkas

# =========================================================#
# 1. IF...ELSE STATEMENT

# --- 1.0 if Statement ---
usia_pasien = int(input("Masukkan usia calon pasien: "))
if usia_pasien >= 17:
    print("Boleh mendaftar sebagai pasien klinik.")
print("Proses registrasi selesai.")

# --- 1.1 if...else Statement
usia_pasien = int(input("Masukkan usia calon pasien: "))
if usia_pasien >= 17:
    print("Registrasi disetujui.")
else:
    print("Registrasi ditolak, usia belum memenuhi syarat.")

# --- 1.2 Verifikasi Login Petugas
username_db = "dokter"
password_db = "klinik@456"
username = input("Masukkan username dokter: ")
password = input("Masukkan password dokter: ")
if (username == username_db) and (password == password_db):
    print("Login berhasil, selamat bertugas.")
else:
    print("Login gagal, akses ditolak.")

# --- 1.3 if...elif...else Statement
usia_pasien = int(input("Masukkan usia calon pasien: "))
if usia_pasien < 0:
    print("Usia tidak valid.")
elif usia_pasien >= 17:
    print("Registrasi disetujui.")
else:
    print("Registrasi ditolak.")

# =========================================================#
# 2. FOR LOOP

# --- 2.0 Iterasi daftar obat ---
daftar_buku = ["Paracetamol", "Vitamin C", "Amoxicillin"]
for obat in daftar_buku:
    print(obat)
    print("---")

# --- 2.1 Iterasi karakter dalam string
kata_kunci = 'Kesehatan'
for huruf in kata_kunci:
    print(huruf)

# --- 2.2 Total Nomor Antrian Pemeriksaan
total_antrian = 0
for i in range(1, 11):
    total_antrian += i
print(f"Total nomor antrian pemeriksaan = {total_antrian}")

# =========================================================#
# 3. WHILE LOOP

# --- 3.0 Infinite while Loop (CONTOH BUG, JANGAN DIJALANKAN LANGSUNG) ---
# Blok ini SENGAJA salah untuk menunjukkan bug klasik: variabel 'stok'
# tidak pernah diperbarui di dalam loop, jadi 'stok >= 0' selamanya True
# -> program tidak akan pernah berhenti sendiri.
# Dibiarkan dalam bentuk komentar supaya file tetap bisa dijalankan penuh.
#
# stok = float(input("Masukkan jumlah stok obat: "))
# while stok >= 0.0:
#     print(stok)

# --- 3.1 Finite while Loop (versi yang sudah diperbaiki)
stok = float(input("Masukkan jumlah stok obat (angka negatif untuk berhenti): "))
while stok >= 0.0:
    print(stok)
    stok = float(input("Masukkan stok obat berikutnya: "))

# --- 3.2 Cetak Nomor Antrian 1 sampai n
n = 10
i = 1
while i <= n:
    print(i)
    i += 1

# --- 3.3 Total Biaya Sampai User Input 0
total_biaya = 0
denda = float(input("Masukkan nominal biaya (0 untuk berhenti): "))
while denda != 0.0:
    total_biaya += denda
    denda = float(input("Masukkan nominal biaya (0 untuk berhenti): "))
print(f"Total biaya terkumpul: Rp{total_biaya}")

# =========================================================#
# 4. BREAK & CONTINUE

# --- 4.0 break dalam for Loop
id_target = int(input("Masukkan nomor pasien yang dicari (1-5): "))
for nomor_pasien in range(1, 6):
    if nomor_pasien == id_target:
        break
    print(nomor_pasien)

# --- 4.1 break dalam while Loop
while True:
    jumlah_input = int(input("Masukkan jumlah pasien datang (negatif untuk berhenti): "))
    if jumlah_input < 0:
        break
    print(f"Pasien datang tercatat: {jumlah_input}")

# --- 4.2 continue dalam for Loop
for nomor_antrian in range(1, 11):
    if nomor_antrian % 2 == 0:
        continue           # lewati nomor antrian genap
    print(nomor_antrian)

# --- 4.3 Total Hanya Denda Positif
total_biaya_valid = 0
while True:
    denda = int(input("Masukkan nominal biaya (0 untuk berhenti): "))
    if denda < 0:
        continue           # abaikan input tidak valid, jangan dihitung
    if denda == 0:
        break
    total_biaya_valid += denda
print(f"Total biaya yang tercatat: Rp{total_biaya_valid}")

# =========================================================#
# 5. PASS STATEMENT

pasien_valid = True
if pasien_valid:
    pass                    # placeholder, logika verifikasi lanjutan belum dibuat
else:
    print("Login tidak valid. Arahkan ke formulir registrasi.")

# =========================================================#
#DATA TYPE#

# 1. NUMBERS
# --- 1.0 int, float, complex
nomor_pasien = 1024                 # int, ID unik pasien
suhu_tubuh = 36.7               # float, suhu tubuh pasien dalam derajat Celsius

# complex dimasukkan supaya materi lengkap sesuai silabus, TAPI jujur:
# di sistem perpustakaan nyata tipe ini nyaris tidak relevan. Contoh di bawah
# dipaksakan biar demonstratif, bukan karena dibutuhkan secara fungsional.
kode_referensi_kompleks = 4 + 2j

print("=== NUMBERS: int, float, complex ===")
print(f"ID Pasien    : {nomor_pasien}  -> {type(nomor_pasien)}")
print(f"Suhu Tubuh   : {suhu_tubuh} -> {type(suhu_tubuh)}")
print(f"Contoh complex: {kode_referensi_kompleks} -> {type(kode_referensi_kompleks)}")

suhu_tubuh = round((suhu_tubuh + 37.0) / 2, 2)   # simulasi rata-rata baru masuk
print(f"Suhu tubuh setelah pemeriksaan ulang: {suhu_tubuh}")

# --- 1.1 Number Systems (binary, octal, hexadecimal)
# Sama seperti complex, ini juga materi wajib silabus yang jarang dipakai
# langsung di sistem perpustakaan. Contoh: kalau rak buku diberi kode heksadesimal.
kode_ruang_hex = 0x2A     # anggap kode rak dalam heksadesimal
kode_ruang_bin = 0b1100   # anggap kode rak dalam biner

print("\n=== NUMBERS: Number Systems ===")
print(f"Kode ruang (hex 0x1F) dalam desimal: {kode_ruang_hex}")
print(f"Kode ruang (bin 0b1010) dalam desimal: {kode_ruang_bin}")

# --- 1.2 Type Conversion pada Numbers
print("\n=== NUMBERS: Type Conversion ===")
print("int(4.9) ->", int(4.9))     # dipotong (truncated), bukan dibulatkan
print("float(5) ->", float(5))
print("complex(3) ->", complex(3))

# --- 1.3 Modul random: rekomendasi buku acak
daftar_buku = ["Paracetamol", "Vitamin C", "Amoxicillin"]
rekomendasi_hari_ini = random.choice(daftar_buku)
print("\n=== NUMBERS: Modul random ===")
print("Obat yang direkomendasikan hari ini:", rekomendasi_hari_ini)

# --- 1.4 Modul math: hitung kebutuhan rak
total_obat_baru = 47
kapasitas_per_laci = 10
jumlah_laci_dibutuhkan = math.ceil(total_obat_baru / kapasitas_per_laci)
print("\n=== NUMBERS: Modul math ===")
print(f"{total_obat_baru} buku baru butuh {jumlah_laci_dibutuhkan} laci (kapasitas {kapasitas_per_laci}/rak)")

# =========================================================#
# 2. LIST

daftar_resep = ["Paracetamol", "Vitamin C"]

print("\n=== LIST (daftar resep) ===")
print(f"Awal            : {daftar_resep} -> {type(daftar_resep)}")

daftar_resep.append("Amoxicillin")   # pasien mendapat obat baru
print(f"Setelah mendapat resep  : {daftar_resep}")

daftar_resep.remove("Vitamin C")      # anggota mengembalikan buku
print(f"Setelah obat dihentikan : {daftar_resep}")
print(f"Jumlah resep aktif: {len(daftar_resep)}")

# =========================================================#
# 3. TUPLE

lokasi_ruang = ("Lantai 1", "Ruang B", 5)   # (lantai, nama rak, nomor slot)

print("\n=== TUPLE (lokasi rak) ===")
print(f"Lokasi ruang pemeriksaan: {lokasi_ruang} -> {type(lokasi_ruang)}")
print(f"Lantai : {lokasi_ruang[0]}")
print(f"Ruang  : {lokasi_ruang[1]}")
print(f"Nomor  : {lokasi_ruang[2]}")
# lokasi_ruang[0] = "Lantai 3"  # akan TypeError -- tuple tidak bisa diubah (immutable)

# =========================================================#
# 4. STRING

judul_buku = "  pemeriksaan umum  "   # sengaja ada spasi & huruf kecil, simulasi input mentah
penulis = "Dr. Andi Pratama"
isbn = "REG-2026-078"

print("\n=== STRING ===")
judul_bersih = judul_buku.strip().title()   # hapus spasi tepi, kapital tiap kata
print(f"Nama layanan mentah   : '{judul_buku}'")
print(f"Nama layanan dibersihkan: '{judul_bersih}'")

print("Panjang nama layanan   :", len(judul_bersih))
print("Nama layanan huruf besar semua:", judul_bersih.upper())
print("Cek kode registrasi diawali '978':", isbn.startswith("978"))
print("Ganti kata di nama layanan:", judul_bersih.replace("Umum", "Khusus"))

# split & join -- pecah nama dokter jadi list kata, gabung lagi dengan format lain
kata_dokter = penulis.split(" ")
print("Split nama dokter:", kata_dokter)
print("Join dengan tanda titik:", ".".join(kata_dokter))

# slicing string
print("4 huruf pertama judul:", judul_bersih[:4])

# f-string formatting (dipakai berkali-kali di file lain juga)
print(f"Layanan '{judul_bersih}' ditangani oleh {penulis} (ISBN: {isbn})")

# =========================================================#
# 5. SET

kategori_buku = {"Umum", "Anak", "Umum", "Gigi", "Anak"}

print("\n=== SET (kategori layanan) ===")
print(f"Kategori tersimpan : {kategori_buku} -> {type(kategori_buku)}")
print(f"Jumlah kategori unik: {len(kategori_buku)}")   # otomatis jadi 3, bukan 5

kategori_buku.add("Laboratorium")     # tambah kategori baru
kategori_buku.add("Fiksi")         # duplikat, tidak akan menambah anggota set
print(f"Setelah add        : {kategori_buku}")

# =========================================================#
# 6. DICTIONARY

profil_pasien = {
    "id_pasien": 3107261845,
    "nama": "Rizky",
    "suhu_tubuh_rata_rata": suhu_tubuh,
    "daftar_resep": daftar_resep,
    "status_aktif": True,
}

print("\n=== DICTIONARY (profil pasien) ===")
print(f"Profil lengkap : {profil_pasien} -> {type(profil_pasien)}")
print(f"Nama           : {profil_pasien['nama']}")
print(f"Status aktif   : {profil_pasien['status_aktif']}")

profil_pasien["status_aktif"] = False   # misal: kena status nonaktif sementara karena kontrol selesai
print(f"Setelah update : status_aktif = {profil_pasien['status_aktif']}")


# =========================================================#
#FUNCTIONS#

# 1. Deklarasi Fungsi Sederhana
def sapa_pasien():
    print("Selamat datang di Klinik Sehat Bersama!")

sapa_pasien()

# 2. Fungsi dengan Argumen (Positional & Default)
def hitung_biaya(jumlah_hari, tarif_per_hari=750):
    total = jumlah_hari * tarif_per_hari
    print(f"Total biaya layanan: Rp{total}")

hitung_biaya(3)          # pakai tarif default
hitung_biaya(5, 1000)    # timpa tarif default dengan 1000

# 3. Fungsi dengan Return Value
def cek_ketersediaan_obat(jumlah_stok_obat):
    if jumlah_stok_obat > 0:
        return "Obat tersedia untuk diberikan"
    else:
        return "Obat sedang habis"

status_obat = cek_ketersediaan_obat(2)
print("Status:", status_obat)

# 4. Global, Local, dan Nonlocal Variable
total_obat_klinik = 500   # global variable

def berikan_obat():
    obat_diberikan_lokal = 2     # local variable -- sengaja beda nama dari
                                # 'obat_terpakai' global di bagian Operators
                                 # biar nggak ketuker pas dibaca ulang
    sisa_obat = total_obat_klinik - obat_diberikan_lokal
    print(f"Sisa obat setelah diberikan: {sisa_obat}")

berikan_obat()

# 5. Fungsi Lambda (Fungsi Anonim)
diskon_biaya = lambda nominal_biaya: nominal_biaya - (nominal_biaya * 0.1)
print(f"Biaya setelah diskon: Rp{diskon_biaya(50000)}")

# 6. Fungsi Rekursif
def biaya_bertingkat(hari):
    if hari == 1:
        return 500
    else:
        return 2 * biaya_bertingkat(hari - 1)

print(f"Biaya bertingkat hari ke-4: Rp{biaya_bertingkat(4)}")

# 7. Penggunaan Module
# math sudah di-import di baris paling atas file -- dipakai ulang di sini
# supaya tidak import dobel, cukup satu kali di awal untuk seluruh file.
biaya_mentah = 6875.10
biaya_dibulatkan = math.ceil(biaya_mentah)
print(f"Biaya dibulatkan ke atas: Rp{biaya_dibulatkan}")