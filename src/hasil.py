import os
import time
import locale
from fungsi import baca_fail

locale.setlocale(locale.LC_TIME, "id_ID")


def hasil(data, kode):
    koleksi_format = {
        "cty": data[kode]["@description"],
        "prv": data[kode]["@domain"],
        "ltg": data[kode]["@latitude"],
        "bjr": data[kode]["@longitude"],
        "dt": time.strftime("%d %B %Y"),
        "h0": data[kode]["parameter"][0]["timerange"][0]["value"]["#text"] + "%",
        "h1": data[kode]["parameter"][0]["timerange"][1]["value"]["#text"] + "%",
        "h2": data[kode]["parameter"][0]["timerange"][2]["value"]["#text"] + "%",
        "h3": data[kode]["parameter"][0]["timerange"][3]["value"]["#text"] + "%",
        "hx": data[kode]["parameter"][1]["timerange"][0]["value"]["#text"] + "%",
        "hm": data[kode]["parameter"][3]["timerange"][0]["value"]["#text"] + "%",
        "t0": data[kode]["parameter"][5]["timerange"][0]["value"][0]["#text"] + "°C",
        "t1": data[kode]["parameter"][5]["timerange"][1]["value"][0]["#text"] + "°C",
        "t2": data[kode]["parameter"][5]["timerange"][2]["value"][0]["#text"] + "°C",
        "t3": data[kode]["parameter"][5]["timerange"][3]["value"][0]["#text"] + "°C",
        "tx": data[kode]["parameter"][2]["timerange"][0]["value"][0]["#text"] + "°C",
        "tm": data[kode]["parameter"][4]["timerange"][0]["value"][0]["#text"] + "°C",
        "w0": data[kode]["parameter"][8]["timerange"][0]["value"][2]["#text"] + " km/j",
        "w1": data[kode]["parameter"][8]["timerange"][1]["value"][2]["#text"] + " km/j",
        "w2": data[kode]["parameter"][8]["timerange"][2]["value"][2]["#text"] + " km/j",
        "w3": data[kode]["parameter"][8]["timerange"][3]["value"][2]["#text"] + " km/j",
        "wk": data[kode]["parameter"][7]["timerange"][0]["value"][1]["#text"],
        "wd": data[kode]["parameter"][7]["timerange"][0]["value"][0]["#text"],
    }
    os.system("cls||clear")
    print(baca_fail('kepala.txt')
          + baca_fail("hasil.txt").format(**koleksi_format))
    input("\rMasukkan [Q] untuk keluar ")
