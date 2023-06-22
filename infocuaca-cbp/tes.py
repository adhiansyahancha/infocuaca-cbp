badInput = True
while badInput:
    filesize = input("Podaj rozmiar pliku i jednostke (np. \"100 mb\", \"130 gb\", \"84 kb\"): ")
    if filesize[-3:] ==  ' mb' or filesize[-3:] == ' kb' or filesize[-3:] == ' gb':
        badInput = False
        print("true")
    else:
        print("Podaj jeszcze raz rozmiar pliku w formacie [liczba format] np. 12 kb")


print(
    f'{3 + 2}'
)