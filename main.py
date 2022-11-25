import requests
import numpy
API_KEY = "d485793245775bad0112e296db963d3a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
namaKota = input("Nama kota : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={namaKota}&lang=id"
respone = requests.get(request_url)
data = respone.json()
lon = data['coord']['lon']
lat = data['coord']['lat']
print(lon, lat)
def cuaca():
    request_url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,precipitation,weathercode,surface_pressure,cloudcover&current_weather=true&timezone=Asia%2FSingapore"
    respone2 = requests.get(request_url2)
    if respone2.status_code == 200:
        data2 = respone2.json()
        weather_now = data2['current_weather']['temperature']
        waktu = data2['current_weather']['time']
        perjam = data2['hourly']['time']
        cuaca_perjam = data2['hourly']['temperature_2m']
        cuaca_seminggu = numpy.column_stack([perjam, cuaca_perjam])
        # print(cuaca_seminggu)
        print(f"Sekarang: {waktu}, Cuaca: {weather_now} derajat Celcius")
        # print(perjam)
        list_cuaca = []
        for i in range (0, len(cuaca_seminggu)):
            list_cuaca.append(cuaca_seminggu[i])
        print(cuaca_seminggu[:24:3])
        # for i in range(len(cuaca_perjam)):
        #     print(type(cuaca_perjam[i]))
        # for i in range(len(cuaca_perjam)):
        #     cuaca_perjam[i] = str(cuaca_perjam[i])
        #     print(type(cuaca_perjam[i]))
        
    else:
        print("An error occured")
cuaca()
