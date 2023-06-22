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
def daftar_kota(api_cuaca) -> list:
    data = []
    
    for kota in range(36):
        data.append(api_cuaca[kota]['@description'])

    return data

# Segarkan konsol
def segarkan_konsol():
    return os.system('cls||clear')

# Uraikan perintah pengguna
def urai_perintah(arg):
    if arg in ('keluar', 'exit', 'quit'):
        exit(0)
    elif arg == 'tentang':
        segarkan_konsol()
        print(
            baca_fail('kepala.txt') +
            baca_fail('tentang.txt')
        )
        input()
    

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
    return masukan

def tes_dapatkan_cuaca(city):      
    # nanti ganti dengan API yang sesungguhnya
    data_kota = {
        "jakarta": "Cerah",
        "bandung": "Berawan",
        "purwokerto": "Hujan sedang",
        "brebes": "Berawan",
        "pekalongan": "Cerah"
    }

    if city in data_kota:
        return data_kota[city]
    else:
        raise ValueError("Kota tidak ditemukan")

    while True:
        try:
            city_input = input("Masukkan nama kota: ")
            city_input = city_input.lower()
            validated_input = validate_input(city_input)
            weather = get_weather(validated_input)
            print("Informasi cuaca untuk", validated_input + ":", weather)
            break

        except ValueError as e:
            print("Error:", e)