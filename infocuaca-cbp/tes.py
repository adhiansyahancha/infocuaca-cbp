import requests
import locale
import time
from fungsi import baca_fail

locale.setlocale(locale.LC_TIME, "id_ID")

data = requests.get(
    "https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json"
).json()["row"]["data"]["forecast"]["area"]

konversi_kota_kode = {}
for kode in range(len(data)):
    konversi_kota_kode[f"{data[kode]['@description']}"] = kode

input_kota = input("Masukkan nama kota: ")
input_kota = input_kota.title().strip()


def data_persiapan(kode):
    return {
        "cty": data[kode]["@description"],
        "prv": data[kode]["@domain"],
        "ltg": data[kode]["@latitude"],
        "bjr": data[kode]["@longitude"],
        "dt": time.strftime('%d %B %Y'),
    }


print(baca_fail("hasil.txt").format(**data_persiapan(konversi_kota_kode[input_kota])))
