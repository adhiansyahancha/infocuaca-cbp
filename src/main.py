import os
import re
import time
import locale
import requests
from fungsi import (
    baca_fail,
    segarkan_konsol,
    cari_kota,
    daftar_kota,
    urutkan_kota,
    konversi_ke_kode,
)

locale.setlocale(locale.LC_TIME, "id_ID")


# Inti eksekusi
def kode_inti(area_cuaca):
    segarkan_konsol()

    print(baca_fail("kepala.txt"))
    print(baca_fail("intro.txt"))
    print(baca_fail("perintah.txt"))

    while True:
        argumen_pengguna = input("infocuaca-processor % ")
        urai_perintah(argumen_pengguna, area_cuaca)


# Panggil untuk mendapatkan respon API
def respon_data_cuaca():
    return requests.get(
        "https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json"
    )


# Uraikan perintah pengguna
def urai_perintah(masukan, area_cuaca):
    if masukan[:4] == 'cari':
        pola = r'^cari "(.*)"$'
        hasil = re.match(pola, masukan)
        try:
            kueri = hasil.group(1)
        except AttributeError:
            print("Pencarian tidak valid\n")
            
        try:
            if kueri:
                hasil_pencarian = cari_kota(urutkan_kota(daftar_kota(area_cuaca)), kueri.title())
                if hasil_pencarian != -1:
                    print(f'Kota \"{kueri.title()}\" ditemukan di pangkalan data\n')
                else:
                    print(f"Hasil pencarian untuk \'{kueri}\' tidak ditemukan")
            else:
                print("Kueri tidak valid")
        except UnboundLocalError:
            print("Pencarian tidak Valid\n")

    elif masukan[:9] == 'tampilkan':
        pola = r'^tampilkan "(.*)"$'  
        hasil = re.match(pola, masukan)
        try:
            kueri = hasil.group(1)
        except AttributeError:
            print("Kueri tidak valid\n")

        if kueri:
            tampilkan(area_cuaca, konversi_ke_kode(area_cuaca)[kueri.title()])
            kode_inti(area_cuaca)
        else:
            print("Kueri tidak valid")

    # Pencocokan untuk perintah non-argumen
    elif masukan == 'daftar-kota':
        daftarkota(area_cuaca)
        kode_inti(area_cuaca)

    elif masukan == 'tentang':
        tentang(area_cuaca)
    elif masukan == 'bersihkan':
        segarkan_konsol()
        kode_inti(area_cuaca)
    elif masukan in ('keluar', 'exit', 'quit'):
        print("Keluar")
        exit(0)
    elif masukan.isspace() or masukan in '':
        pass
    else:
        print(f"Perintah {masukan} tidak valid\n")
        
def daftarkota(area_cuaca):
    segarkan_konsol()
    list_kota = daftar_kota(area_cuaca)
    print(baca_fail('kepala.txt'))
    for kota in list_kota:
        print(f"{list_kota.index(kota)+1}. {kota}")

    input("Masukan Q untuk keluar: ")

def tentang(area_cuaca):
    os.system("cls||clear")
    print("\r" + baca_fail("kepala.txt") + baca_fail("tentang.txt") + "\n")
    input("\rMasukkan [Q] untuk keluar ")
    kode_inti(area_cuaca)


def tampilkan(area_cuaca, kode):
    koleksi_format = {
        "cty": area_cuaca[kode]["@description"],
        "prv": area_cuaca[kode]["@domain"],
        "ltg": area_cuaca[kode]["@latitude"],
        "bjr": area_cuaca[kode]["@longitude"],
        "dt": time.strftime("%d %B %Y"),
        "h0": area_cuaca[kode]["parameter"][0]["timerange"][0]["value"]["#text"] + "%",
        "h1": area_cuaca[kode]["parameter"][0]["timerange"][1]["value"]["#text"] + "%",
        "h2": area_cuaca[kode]["parameter"][0]["timerange"][2]["value"]["#text"] + "%",
        "h3": area_cuaca[kode]["parameter"][0]["timerange"][3]["value"]["#text"] + "%",
        "hx": area_cuaca[kode]["parameter"][1]["timerange"][0]["value"]["#text"] + "%",
        "hm": area_cuaca[kode]["parameter"][3]["timerange"][0]["value"]["#text"] + "%",
        "t0": area_cuaca[kode]["parameter"][5]["timerange"][0]["value"][0]["#text"]
        + "°C",
        "t1": area_cuaca[kode]["parameter"][5]["timerange"][1]["value"][0]["#text"]
        + "°C",
        "t2": area_cuaca[kode]["parameter"][5]["timerange"][2]["value"][0]["#text"]
        + "°C",
        "t3": area_cuaca[kode]["parameter"][5]["timerange"][3]["value"][0]["#text"]
        + "°C",
        "tx": area_cuaca[kode]["parameter"][2]["timerange"][0]["value"][0]["#text"]
        + "°C",
        "tm": area_cuaca[kode]["parameter"][4]["timerange"][0]["value"][0]["#text"]
        + "°C",
        "w0": area_cuaca[kode]["parameter"][8]["timerange"][0]["value"][2]["#text"]
        + " km/j",
        "w1": area_cuaca[kode]["parameter"][8]["timerange"][1]["value"][2]["#text"]
        + " km/j",
        "w2": area_cuaca[kode]["parameter"][8]["timerange"][2]["value"][2]["#text"]
        + " km/j",
        "w3": area_cuaca[kode]["parameter"][8]["timerange"][3]["value"][2]["#text"]
        + " km/j",
        "wk": area_cuaca[kode]["parameter"][7]["timerange"][0]["value"][1]["#text"],
        "wd": area_cuaca[kode]["parameter"][7]["timerange"][0]["value"][0]["#text"],
    }
    os.system("cls||clear")
    print(baca_fail("kepala.txt") + baca_fail("hasil.txt").format(**koleksi_format))
    input("\rMasukkan [Q] untuk keluar ")


if __name__ == "__main__":
    segarkan_konsol()
    print(baca_fail("kepala.txt"))
    print("Memuat data...")

    try:
        r = respon_data_cuaca().status_code
    except requests.exceptions.ConnectionError as err:
        print(f"Gagal menghubungkan API. Berikut ini errornya:\n{err}")
        input()

    respon_json_cuaca = respon_data_cuaca().json()
    area_cuaca = respon_json_cuaca["row"]["data"]["forecast"]["area"]

    kode_inti(area_cuaca=area_cuaca)
