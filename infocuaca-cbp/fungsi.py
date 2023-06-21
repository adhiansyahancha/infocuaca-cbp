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
def daftar_kota(data_api) -> list:
    data = []
    
    for kota in range(36):
        data.append(data_api[kota]['@description'])

    return data

# Urutkan kota yang diambil dari daftar_kota
def urutkan_kota(koleksi) -> list:
    for z in range(len(koleksi)):
        for x in range(len(koleksi) - 1):
            if koleksi[x] < koleksi[x + 1]:
                koleksi[x], koleksi[x + 1] = koleksi[x + 1], koleksi[x]

    return koleksi

# Validasikan input agar sesuai ketentuan
def validasi_input(masukan) -> str:
    masukan = masukan.strip()
    pattern = r"^[a-zA-Z]+$"
    if not re.match(pattern, masukan):
        raise ValueError("Input hanya boleh berisi huruf alfabet")

    return masukan