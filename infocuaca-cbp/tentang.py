import os
from fungsi import baca_fail

def tentang():
    os.system('cls||clear')
    print('\r' + baca_fail('kepala.txt') + baca_fail('tentang.txt') + '\n')
    input("\rMasukkan [Q] untuk keluar ")