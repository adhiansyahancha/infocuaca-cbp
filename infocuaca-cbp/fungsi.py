import os
import re

# Baca fail dari direktori 'display'
def baca_fail(fail) -> None:
    DIR_FAIL = os.path.join(os.path.dirname(__file__).replace('infocuaca-cbp', '') + 'display', f'{fail}')
    with open(DIR_FAIL, encoding='utf-8') as _fail:
        return _fail.read()

# Cari kota di data yang sudah disiapkan daftar_kota
def cari_kota(data_kota, kueri) -> str:
    batas_awal = 0
    batas_akhir = len(data_kota)
    while batas_awal <= batas_akhir:
        mid_index = (batas_awal + batas_akhir) // 2
        if data_kota[mid_index] < kueri:
            batas_awal = mid_index + 1
        elif data_kota[mid_index] > kueri:
            batas_akhir = mid_index -1
        else:
            return mid_index
    
    return 0

# Tampilkan daftar kota-kota Jawa Tengah
def daftar_kota(json_api) -> list:
    data = []
    
    for kota in range(36):
        data.append(json_api['row']['data']['forecast']['area'][kota]['@description'])

    return data

# Segarkan tampilan
def segarkan_konsol():
    return os.system('cls||clear')

# Uraikan input pengguna
def uraikan_perintah(arg, json_api=None):
    match arg:
        case 'daftar-kota': 
            print(urutkan_kota(daftar_kota(json_api)))
        case 'keluar' | 'exit' | 'quit':
            exit(1)
        case '':
            pass
        case _:
            print("Perintah tidak valid")

# Urutkan kota yang diambil dari daftar_kota
def urutkan_kota(koleksi) -> list:
    for z in range(len(koleksi)):
        for x in range(len(koleksi) - 1):
            if koleksi[x] > koleksi[x + 1]:
                koleksi[x], koleksi[x + 1] = koleksi[x + 1], koleksi[x]

    return koleksi

# Validasikan input agar sesuai ketentuan
def validasi_input(masukan) -> str:
    masukan = masukan.strip()
    pattern = r"^[a-zA-Z]+$"
    if not re.match(pattern, masukan):
        raise ValueError("Input hanya boleh berisi huruf alfabet")

    return masukan