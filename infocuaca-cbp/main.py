import re
import requests
from tentang import tentang
from fungsi import (
    baca_fail,
    segarkan_konsol,
    cari_kota,
    daftar_kota,
    urutkan_kota
)


# Inti eksekusi
def kode_inti(respon_api):
    segarkan_konsol()

    print(baca_fail("kepala.txt") + baca_fail("intro.txt") + baca_fail("perintah.txt"))

    while True:
        argumen_pengguna = input("infocuaca-cbp> ")
        urai_perintah(argumen_pengguna, respon_api)


# Panggil untuk mendapatkan respon API
def respon_data_cuaca():
    return requests.get(
        "https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json"
    )


# Uraikan perintah pengguna
def urai_perintah(masukan, respon_api):
    # Penanganan argumen pencarian
    if 'cari' in masukan:
        masukan = masukan.split(' ')
        pola = r'[^\w\s]'
        hasil = re.sub(pola, '', masukan[1]).title()
        kota_kota = daftar_kota(respon_api)
        if hasil in kota_kota:
            print("hasil ditemukan: ", hasil)
        else:
            print("tidak ditemukan")
    # Pola pencocokan untuk masukan tanpa argumen
    else:
        match masukan:
            case "daftar-kota":
                print(daftar_kota(respon_api), "\n")
            case "tentang":
                tentang()
                kode_inti(respon_api)
            case "keluar" | "exit" | "quit":
                print("Keluar")
                exit(0)
            case "":
                pass
            case _:
                print(f'Perintah "{masukan}" tidak dapat dikenali\n')


if __name__ == "__main__":
    segarkan_konsol()
    print(baca_fail("kepala.txt") + "Memuat...")

    try:
        r = respon_data_cuaca().status_code
    except requests.exceptions.ConnectionError as err:
        print(f"Gagal menghubungkan API. Berikut ini errornya:\n{err}")

    respon_json_cuaca = respon_data_cuaca().json()
    area_cuaca = respon_json_cuaca["row"]["data"]["forecast"]["area"]

    kode_inti(respon_api=area_cuaca)
