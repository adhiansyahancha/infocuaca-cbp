import re
import requests
from tentang import tentang
from hasil import hasil
from fungsi import (
    baca_fail,
    segarkan_konsol,
    cari_kota,
    daftar_kota,
    urutkan_kota,
    konversi_ke_kode
)


# Inti eksekusi
def kode_inti(respon_api):
    segarkan_konsol()

    print(baca_fail("kepala.txt")
          + baca_fail("intro.txt")
          + baca_fail("perintah.txt"))

    while True:
        argumen_pengguna = input("infocuaca-processor % ")
        urai_perintah(argumen_pengguna, respon_api)


# Panggil untuk mendapatkan respon API
def respon_data_cuaca():
    return requests.get(
        "https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json"
    )


# Uraikan perintah pengguna
def urai_perintah(masukan, respon_api):
    # Penanganan argumen pencarian
    if 'cari' in masukan and '"' in masukan:
        masukan = masukan.split(' ')
        try:
            masukan[1] = masukan[1] + ' ' + masukan[2]
        except IndexError:
            pass
        else:
            pass

        pola = r'[^\w\s]'
        kueri = re.sub(pola, '', masukan[1])
        kota_kota = daftar_kota(respon_api)
        hasil_pencarian = cari_kota(urutkan_kota(kota_kota), kueri=kueri.title())

        if hasil_pencarian != 0:
            print(f"Hasil pencarian menemukan {urutkan_kota(kota_kota)[hasil_pencarian]} di pangkalan data\n")
        else:
            print(f"\"{kueri}\" tidak dapat ditemukan")
    elif 'tampilkan' in masukan and '"' in masukan:
        masukan = masukan.split(' ')
        try:
            masukan[1] = masukan[1] + ' ' + masukan[2]
        except IndexError:
            pass
        else:
            pass

        pola = r'[^\w\s+]'
        kueri = re.sub(pola, '', masukan[1])
        # try:
        kode_kueri = konversi_ke_kode(respon_api)[kueri.title()]
        hasil(respon_api, kode_kueri)
        kode_inti(respon_api)
        # except KeyError:
        #     print(f"Kueri {kueri} tidak dapat ditemukan\n")
        # except UnboundLocalError:
        #     print("Kueri tidak valid")

    # Pola pencocokan untuk masukan tanpa argumen
    else:
        match masukan:
            case "daftar-kota":
                print(daftar_kota(respon_api), "\n")
            case "bersihkan":
                segarkan_konsol()
                kode_inti(respon_api)
            case "tentang":
                tentang()
                kode_inti(respon_api)
            case "keluar" | "exit" | "quit":
                print("Keluar")
                exit(0)
            case "":
                pass
            case _:
                print('Perintah tidak dapat dikenali\n')


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
