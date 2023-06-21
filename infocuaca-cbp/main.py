import requests
from fungsi import baca_fail, segarkan_konsol, uraikan_perintah

segarkan_konsol()
print(baca_fail('kepala.txt') + "Memuat...")
json_bmkg = requests.get("https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json").json()

def main():
    # Ambil data area cuaca
    data_dasar = json_bmkg['row']['data']['forecast']['area']
    if type(data_dasar) == list:
        segarkan_konsol()

    print(
        baca_fail('kepala.txt') +
        baca_fail('intro.txt') +
        baca_fail('perintah.txt')
    )


if __name__ == '__main__':
    main()
    while True:
        mp = input('infocuaca-cbp> ')
        uraikan_perintah(mp, json_api=json_bmkg)
        