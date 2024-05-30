import pandas as pd
import matplotlib.pyplot as plt

# Membuat data frame info_mahasiswa
fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]
info_mahasiswa = pd.DataFrame({"Fakultas": fakultas, "Jumlah Mahasiswa": jumlah_mahasiswa, "Akreditasi": akreditasi})

# Membuat diagram batang dengan matplotlib
plt.figure(figsize=(10, 6))
plt.bar(info_mahasiswa["Fakultas"], info_mahasiswa["Jumlah Mahasiswa"], color=['#FF7F50', '#B8860B', '#3CB371', '#00BFFF', '#FF00FF'])
plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')
plt.xticks(rotation=0)
plt.show()
