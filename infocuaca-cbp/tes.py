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

def data_persiapa1(kode):
    return {
        "cty": data[kode]["@description"],
        "prv": data[kode]["@domain"],
        "ltg": data[kode]["@latitude"],
        "bjr": data[kode]["@longitude"],
        "dt": time.strftime('%d %B %Y'),
        "h0": data[kode]["parameter"][0]["timerange"][0]["value"]["#text"],
        "h1": data[kode]["parameter"][0]["timerange"][1]["value"]["#text"],
        "h2": data[kode]["parameter"][0]["timerange"][2]["value"]["#text"],
        "h3": data[kode]["parameter"][0]["timerange"][3]["value"]["#text"],
        "hx": data[kode]["parameter"][1]["timerange"][0]["value"]["#text"],
        "hm": data[kode]["parameter"][3]["timerange"][0]["value"]["#text"],
        "t0": data[kode]["parameter"][5]["timerange"][0]["value"]["#text"],
        "t1": data[kode]["parameter"][5]["timerange"][1]["value"]["#text"],
        "t2": data[kode]["parameter"][5]["timerange"][2]["value"]["#text"],
        "t3": data[kode]["parameter"][5]["timerange"][3]["value"]["#text"],
        "tx": data[kode]["parameter"][2]["timerange"][0]["value"][0]["#text"],
        "tm": data[kode]["parameter"][4]["timerange"][0]["value"][0]["#text"],
        "w0": data[kode]["parameter"][8]["timerange"][0]["value"][2]["#text"],
        "w1": data[kode]["parameter"][8]["timerange"][1]["value"][2]["#text"],
        "w2": data[kode]["parameter"][8]["timerange"][2]["value"][2]["#text"],
        "w3": data[kode]["parameter"][8]["timerange"][3]["value"][2]["#text"],
        "wk": data[kode]["parameter"][7]["timerange"][0]["value"][1]["#text"],
        "wd": data[kode]["parameter"][7]["timerange"][0]["value"][0]["#text"],
    }

print(baca_fail("hasil.txt").format(**data_persiapan(0)))
