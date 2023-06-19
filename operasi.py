"""
Berkas ini berisi operasi-operasi untuk pengolahan prakiraan cuaca
"""

def urutkan_kota(array):
    for z in range(len(array)):
        for x in range(len(array) - 1):
            if array[x] < array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]

    return array

