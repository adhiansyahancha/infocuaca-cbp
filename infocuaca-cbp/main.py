import requests
from fungsi import baca_fail, segarkan_konsol, cari_kota, daftar_kota, urutkan_kota
from tentang import tentang

# Inti eksekusi
def program_inti(data_area_cuaca):
    segarkan_konsol()

    print(baca_fail('kepala.txt') + baca_fail('intro.txt') + baca_fail('perintah.txt'))

    while True:
        argumen_pengguna = input('infocuaca-cbp> ')
        urai_perintah(argumen_pengguna, data_area_cuaca)

# Panggil untuk mendapatkan respon API
def respon_json_cuaca():
    return requests.get("https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json").json()

# Uraikan perintah pengguna
def urai_perintah(masukan, apidata):
    # Penanganan argumen pencarian
    if masukan[:4] == 'cari':
        masukan = masukan.split(' ')
        kueri = masukan[1].title()
        try:
            if masukan[2]:
                kueri = (masukan[1] + ' ' + masukan[2]).title()
        except IndexError:
            pass

        data_kota = urutkan_kota(daftar_kota(apidata))
        hasil_pencarian = cari_kota(data_kota=data_kota, kueri=kueri)

        if kueri in ('', ' '):
            print("Pencarian tidak valid\n")
        elif hasil_pencarian != 0:
            print(f"Ditemukan \"{data_kota[hasil_pencarian]}\" di basis data\n")
        else:
            print("Tidak ditemukan hasil pencarian\n")
    
    # Pola pencocokan untuk masukan tanpa argumen
    else:
        match masukan:
            case 'daftar-kota':
                print(urutkan_kota(daftar_kota(apidata)), '\n')
            case 'tentang':
                tentang()
                program_inti(apidata)
            case 'keluar' | 'exit' | 'quit':
                print("Keluar")
                exit(0)
            case '':
                pass
            case _:
                print("Perintah tidak valid")

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

    program_inti(data_area_cuaca=data_area_cuaca)

        