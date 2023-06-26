import requests

def get_weather(city):
    url = f"https://cuaca.umkt.ac.id/api/cuaca/DigitalForecast-JawaTengah.xml?format=json"

    try:
        response = requests.get(url)
        data = response.json()

        # Mencari data cuaca berdasarkan kota
        for area in data["DaftarCuaca"]["Row"]:
            if area["Kota"].lower() == city.lower():
                cuaca_desk = area["Cuaca"]
                temperatur = area["Suhu"]
                kelembapan = area["Kelembapan"]
                kecepanatan_angin = area["KecepatanAngin"]

        # Menampilkan informasi cuaca
        print(f"Informasi Cuaca untuk kota {city}: ")
        print("Cuaca saat ini: ", cuaca_desk)
        print("Suhu: ", temperatur, "°C")
        print("Kelembapan: ", kelembapan, "%")
        print("Kecepatan angin: ", kecepatan_angin, "km/h")
    except Exception:
        print("Ada Kesalahan")
    
