# Untuk tes saja
wdae = input("Tes cari: ")
if 'cari' in wdae:
    masukan = wdae.split()
    if '\"' not in masukan[1]:
        print("Pencarian tidak dikenali")
        exit()

    masukan[1] = masukan[1].replace('"', '')
    print(masukan)