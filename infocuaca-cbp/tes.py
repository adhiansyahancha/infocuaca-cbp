import requests
import locale
import time
from fungsi import baca_fail

locale.setlocale(locale.LC_TIME, "id_ID")

# data = requests.get(
#     "https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json"
# ).json()["row"]["data"]["forecast"]["area"]

# konversi_kota_kode = {}
# for kode in range(len(data)):
#     konversi_kota_kode[f"{data[kode]['@description']}"] = kode

# input_kota = input("Masukkan nama kota: ")
# input_kota = input_kota.title().strip()


def data_persiapan(kode):
    return {
        "cty": 'Purwokerto',
        "prv": 'Jawa Tengah',
        "ltg": '-7.13456',
        "bjr": '11.1234567',
        "dt": time.strftime('%d %B %Y'),
        "h0": '30%',
        "h1": '30%',
        "h2": '30%',
        "h3": '30%',
        "hx": '30%',
        "hm": '30%',
        "t0": '30°C',
        "t1": '30°C',
        "t2": '30°C',
        "t3": '30°C',
        "tx": '30°C',
        "tm": '30°C',
        "w0": '9 km',
        "w1": '9 km',
        "w2": '9 km',
        "w3": '9 km',
        "wk": 'SE',
        "wd": '112'
    }


print(baca_fail("hasil.txt").format(**data_persiapan(0)))
