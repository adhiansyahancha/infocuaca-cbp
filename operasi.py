import re
"""
Berkas ini berisi operasi-operasi untuk pengolahan prakiraan cuaca
"""

def validasi_input(input_str):
    # Contoh inputan
    # user_input = input("Masukkan input: ")

    # try:
    #     validated_input = validate_input(user_input)
    #     print("Kota yang dimasukkan:", validated_input)
    # except ValueError as e:
    #     print("Error:", e)
    
    input_str = input_str.strip()
    pattern = r"^[a-zA-Z]+$"
    if not re.match(pattern, input_str):
        raise ValueError("Input hanya boleh berisi huruf alfabet")

    return input_str

def urutkan_kota(array):
    for z in range(len(array)):
        for x in range(len(array) - 1):
            if array[x] < array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]

    return array

def daftar_kota(data_api):
    data = []
    
    for kota in range(36):
        data.append(data_api[kota]['@description'])

    return data

def cari_kota(data_kota):
    # Dengan syarat bahwa data telah terurut
    batas_awal = 0
    batas_akhir = len(data_kota)
    while batas_awal <= batas_akhir:
        mid_index = (batas_awal + batas_akhir) // 2
        if data_kota[mid_index] < keyword:
            batas_awal = mid_index + 1
        elif data_kota[mid_index] > keyword:
            batas_akhir = mid_index -1
        else:
            return mid_index
    
    return 0