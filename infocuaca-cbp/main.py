import re
import requests
from fungsi import baca_fail, segarkan_konsol, cari_kota, daftar_kota, urutkan_kota
from tentang import tentang

# Inti eksekusi
def kode_inti(data_area_cuaca):
    segarkan_konsol()

    print(baca_fail('kepala.txt') + baca_fail('intro.txt') + baca_fail('perintah.txt'))

    while True:
        argumen_pengguna = input('infocuaca-cbp> ')
        urai_perintah(argumen_pengguna, data_area_cuaca)

# Panggil untuk mendapatkan respon API
def respon_json_cuaca():
    return requests.get("https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json").json()

# Uraikan perintah pengguna
def urai_perintah(masukan, data_area_cuaca):
    # Penanganan argumen pencarian
    if 'cari' in masukan:
        masukan = masukan.split(' ')
        pola = r'[^\w\s]' 
        hasil = re.sub(pola, '', masukan[1])
        print(hasil)
    # Pola pencocokan untuk masukan tanpa argumen
    else:
        match masukan:
            case 'daftar-kota':
                print(daftar_kota(data_area_cuaca), '\n')
            case 'tentang':
                tentang()
                kode_inti(data_area_cuaca)
            case 'keluar' | 'exit' | 'quit':
                print("Keluar")
                exit(0)
            case '':
                pass
            case _:
                print(f"Perintah \"{masukan}\" tidak dapat dikenali\n")

if __name__ == '__main__':
    segarkan_konsol()
    print(baca_fail('kepala.txt') + "Memuat...")

    data_area_cuaca = None
    try:
        data_area_cuaca = respon_json_cuaca()['row']['data']['forecast']['area']
    except Exception as e:
        print(f"Gagal menghubungkan API cuaca. Berikutt ini errornya:\n{e}")
    else:
        pass

    kode_inti(data_area_cuaca=data_area_cuaca)

        