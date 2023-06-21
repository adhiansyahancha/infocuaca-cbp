import requests
from fungsi import baca_fail, segarkan_konsol, validasi_input, daftar_kota

# Mulai
print(baca_fail('kepala.txt') + "Memuat...")

# Muatkan data API cuaca
json_bmkg = requests.get("https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json").json()
data_dasar = json_bmkg['row']['data']['forecast']['area']
if type(data_dasar) == list:
    segarkan_konsol()

print(
    baca_fail('kepala.txt') +
    baca_fail('intro.txt') +
    baca_fail('perintah.txt')
)

argumen_pengguna = input("infocuaca> ")
if argumen_pengguna == 'daftar-kota':
    print(daftar_kota(data_dasar))


input()