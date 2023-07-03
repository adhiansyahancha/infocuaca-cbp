import os


# Baca fail dari direktori 'display'
def baca_fail(fail) -> None:
    DIR_FAIL = os.path.join(
        os.path.dirname(__file__).replace("src", "") + "display", f"{fail}"
    )
    with open(DIR_FAIL, encoding="utf-8") as _fail:
        return _fail.read()


# Cari kota di data yang sudah disiapkan daftar_kota
def cari_kota(data_kota, kueri) -> int:
    batas_awal = 0
    batas_akhir = len(data_kota) - 1
    while batas_awal <= batas_akhir:
        mid_index = (batas_awal + batas_akhir) // 2
        
        if data_kota[mid_index] < kueri:
            batas_awal = mid_index + 1
        elif data_kota[mid_index] > kueri:
            batas_akhir = mid_index - 1
        else:
            return mid_index

    return -1


# Tampilkan daftar kota-kota Jawa Tengah
def daftar_kota(api_cuaca) -> list:
    data = []

    for kota in range(len(api_cuaca)):
        data.append(api_cuaca[kota]["@description"])

    return data


# Konversi nama kota ke kode untuk API
def konversi_ke_kode(data):
    konversi = {}
    for kode in range(len(data)):
        konversi[f"{data[kode]['@description']}"] = kode

    return konversi


# Segarkan konsol
def segarkan_konsol() -> int:
    return os.system("cls||clear")


# Urutkan kota yang diambil dari daftar_kota
def urutkan_kota(koleksi) -> list:
    for _ in range(len(koleksi)):
        for x in range(len(koleksi) - 1):
            if koleksi[x] > koleksi[x + 1]:
                koleksi[x], koleksi[x + 1] = koleksi[x + 1], koleksi[x]

    return koleksi
