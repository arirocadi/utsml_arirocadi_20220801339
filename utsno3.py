# Data Set
data = [
    {"hari": "senin", "datang": 2, "biaya": 30000 * 2, "mahasiswa": "ani"},
    {"hari": "selasa", "datang": 3, "biaya": 35000 * 3, "mahasiswa": "budi"},
    {"hari": "rabu", "datang": 4, "biaya": 25000 * 4, "mahasiswa": "jono"},
    {"hari": "kamis", "datang": 1, "biaya": 15000 * 1, "mahasiswa": "lono"},
    {"hari": "jumat", "datang": 2, "biaya": 20000 * 2, "mahasiswa": "joni"},
    {"hari": "sabtu", "datang": 5, "biaya": 30000 * 5, "mahasiswa": "ani"},
    {"hari": "minggu", "datang": 2, "biaya": 35000 * 2, "mahasiswa": "budi"}
]

# a) Berapa rata-rata mahasiswa datang pada minggu ini?
total_datang = sum(entry["datang"] for entry in data)
rata_rata_datang = total_datang / len(data)

# b) Kapan biaya tertinggi terjadi?
biaya_tertinggi = max(data, key=lambda x: x["biaya"])

# c) Hari apa biaya lebih dari 110000?
biaya_lebih_110k = [entry["hari"] for entry in data if entry["biaya"] > 110000]

# d) Siapa yang paling banyak datang ke kampus?
datang_per_mahasiswa = {}
for entry in data:
    mahasiswa = entry["mahasiswa"]
    datang_per_mahasiswa[mahasiswa] = datang_per_mahasiswa.get(mahasiswa, 0) + entry["datang"]
paling_banyak_datang = max(datang_per_mahasiswa, key=datang_per_mahasiswa.get)

# e) Siapa yang datang pada hari minggu?
datang_minggu = [entry["mahasiswa"] for entry in data if entry["hari"] == "minggu"]

# f) Berapa biaya tertinggi dan terendah?
biaya_tertinggi_nilai = max(entry["biaya"] for entry in data)
biaya_terendah_nilai = min(entry["biaya"] for entry in data)

# g) Berapa frekuensi datang tertinggi dan terendah?
frekuensi_datang_tertinggi = max(entry["datang"] for entry in data)
frekuensi_datang_terendah = min(entry["datang"] for entry in data)

# Print the results
print(f"a) Rata-rata mahasiswa datang pada minggu ini: {rata_rata_datang}")
print(f"b) Biaya tertinggi terjadi pada hari {biaya_tertinggi['hari']} dengan biaya {biaya_tertinggi['biaya']}")
print(f"c) Hari dengan biaya lebih dari 110000: {', '.join(biaya_lebih_110k)}")
print(f"d) Mahasiswa yang paling banyak datang ke kampus: {paling_banyak_datang}")
print(f"e) Mahasiswa yang datang pada hari minggu: {', '.join(datang_minggu)}")
print(f"f) Biaya tertinggi: {biaya_tertinggi_nilai}, Biaya terendah: {biaya_terendah_nilai}")
print(f"g) Frekuensi datang tertinggi: {frekuensi_datang_tertinggi}, Frekuensi datang terendah: {frekuensi_datang_terendah}")
