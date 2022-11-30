import requests
import numpy


API_KEY = "d485793245775bad0112e296db963d3a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
namaKota = input("Nama kota : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={namaKota}&lang=id"
respone = requests.get(request_url)
data = respone.json()
lon = data['coord']['lon'] #longitude
lat = data['coord']['lat'] #latitude
print(lat, lon)

request_url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,precipitation,weathercode,surface_pressure,cloudcover&current_weather=true&timezone=Asia%2FSingapore"
respone2 = requests.get(request_url2)

if respone2.status_code == 200:
    data2 = respone2.json()
    weather_now = data2['current_weather']['temperature']
    waktu = data2['current_weather']['time']
    perjam = data2['hourly']['time']
    listCuacaPerjam = []
    cuaca_perjam = data2['hourly']['temperature_2m']
    for i in range(len(cuaca_perjam)):
        cuaca_perjam[i] = str(cuaca_perjam[i])
        listCuacaPerjam.append(cuaca_perjam[i] + " C")

    listKelembaban = []
    kelembaban = data2['hourly']['relativehumidity_2m']
    for i in range(len(kelembaban)):
        kelembaban[i] = str(kelembaban[i])
        listKelembaban.append(kelembaban[i] + " %")

    listPresipitasi = []
    precipitasi = data2['hourly']['precipitation']
    for i in range(len(precipitasi)):
        precipitasi[i] = str(precipitasi[i])
        listPresipitasi.append(precipitasi[i] + " mm")

    listTekananUdara = []
    tekanan_permukaan = data2['hourly']['surface_pressure']
    for i in range(len(tekanan_permukaan)):
        tekanan_permukaan[i] = str(tekanan_permukaan[i])
        listTekananUdara.append(tekanan_permukaan[i] + " Pa")
        
    kode_cuaca = data2['hourly']['weathercode']
    for i in range(len(kode_cuaca)):
        if kode_cuaca[i] == 0:
            kode_cuaca[i] = "Langit cerah"
        elif kode_cuaca[i] == 2:
            kode_cuaca[i] = "Sedikit berawan"
        elif kode_cuaca[i] == 3:
            kode_cuaca[i] = "Mendung"
        elif kode_cuaca[i] == 45 or kode_cuaca[i] == 48:
            kode_cuaca[i] = "Berkabut"
        elif kode_cuaca[i] == 51 or kode_cuaca[i] == 53 or kode_cuaca[i] == 55:
            kode_cuaca[i] = "Rintik-rintik"
        elif kode_cuaca[i] == 56 or kode_cuaca[i] == 57:
            kode_cuaca[i] = "Rintik-rintik, sedikit bersalju"
        elif kode_cuaca[i] == 61 or kode_cuaca[i] == 63 or kode_cuaca[i] == 65:
            kode_cuaca[i] = "Gerimis"
        elif kode_cuaca[i] == 66 or kode_cuaca[i] == 67:
            kode_cuaca[i] = "Gerimis, sedikit bersalju"
        elif kode_cuaca[i] == 71 or kode_cuaca[i] == 73 or kode_cuaca[i] == 75:
            kode_cuaca[i] = "Sedikit bersalju"
        elif kode_cuaca[i] == 77:
            kode_cuaca[i] = "Butiran salju turun"
        elif kode_cuaca[i] == 80 or kode_cuaca[i] == 81 or kode_cuaca[i] == 82:
            kode_cuaca[i] = "Hujan ringan"
        elif kode_cuaca[i] == 85 or kode_cuaca[i] == 86:
            kode_cuaca[i] = "Hujan salju ringan"
        elif kode_cuaca[i] == 95:
            kode_cuaca[i] = "Hujan lebat disertai petir"
        elif kode_cuaca[i] == 96 or kode_cuaca[i] == 99:
            kode_cuaca[i] = "Hujan lebat disertai hujan es" #Only available in central europe
    
    cuaca_seminggu = numpy.column_stack([perjam, listCuacaPerjam, listKelembaban, listPresipitasi, listTekananUdara, kode_cuaca])
    print(f"Sekarang: {waktu}, Cuaca: {weather_now} derajat Celcius")
    print("ini cuaca sehari kelipatan 3\n",cuaca_seminggu[:24:3])
    print("ini cuaca seminggu\n",cuaca_seminggu[::24])
else:
    print("An error occured")
