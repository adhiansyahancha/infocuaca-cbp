import requests
from fungsi import baca_fail, segarkan_konsol, daftar_kota

segarkan_konsol()
print(baca_fail('kepala.txt') + "Memuat...")

json_bmkg = requests.get("https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json").json()
data_dasar = json_bmkg['row']['data']['forecast']['area']

# Uraikan perintah pengguna
def urai_perintah(masukan):
    # Pola pencocokan untuk masukan tanpa argumen
    match masukan.lower():
        case 'daftar-kota':
            print(daftar_kota(data_dasar))
        case 'keluar' | 'exit' | 'quit':
            print("Keluar")
            exit(0)
    

if __name__ == '__main__':
    if type(data_dasar) == list:
        segarkan_konsol()

    print(
        baca_fail('kepala.txt') +
        baca_fail('intro.txt') +
        baca_fail('perintah.txt')
    )

    while True:
        argumen_pengguna = input('infocuaca-cbp> ')
        urai_perintah(argumen_pengguna)
        