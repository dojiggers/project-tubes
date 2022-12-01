import requests


API_KEY = "bab49de27682105d94789820f4404b5e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
BASE_URL2 = "http://api.openweathermap.org/data/2.5/forecast"

namaKota = input("Nama kota : ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={namaKota}&lang=id"
respone = requests.get(request_url)
data = respone.json()
lon = data['coord']['lon'] #longitude
lat = data['coord']['lat'] #latitude
print(lat, lon)
request_url2 = f"{BASE_URL2}?lat={lat}&lon={lon}&appid={API_KEY}&lang=id"
respon = requests.get(request_url2)
data2 = respon.json()

list = data2['list']

def listWaktu(n):
    list_waktu = []
    for i in range(len(list)):
        list_waktu.append(list[i]['dt_txt'])
    print(list_waktu[n])
listWaktu(2)

def listTemperature(n):    
    list_temp = []
    for i in range(len(list)):
        list_temp.append(round(list[i]['main']['temp'] - 273.15, 1))
    print(f"Temperatur : {list_temp[n]} Celcius")
listTemperature(2)

def listPressure(n):
    list_pressure = []
    for i in range(len(list)):
        list_pressure.append(list[i]['main']['pressure'])
    print(f"Tekanan : {list_pressure[n]} Pa")
listPressure(2)

def listHumidity(n):
    list_humidity = []
    for i in range(len(list)):
        list_humidity.append(list[i]['main']['humidity'])
    print(f"Kelembaban : {list_humidity[n]} %")
listHumidity(2)

def listWeatherMain(n):
    list_weather_main = []
    for i in range(len(list)):
        list_weather_main.append(list[i]['weather'][0]['main'])
    print(list_weather_main[n])
#listWeatherMain(0) #Kalo perlu aja mad

def listWeatherDesc(n):
    list_weather_description = []
    for i in range(len(list)):
        list_weather_description.append(list[i]['weather'][0]['description'])
    print(f"Kondisi : {list_weather_description[n]}")
listWeatherDesc(2)

def listWeatherIcon(n):
    list_weather_icon = []
    for i in range(len(list)):
        list_weather_icon.append(list[i]['weather'][0]['icon'])
    print(list_weather_icon[n])
listWeatherIcon(2)

def listPrecipitation(n):
    list_pop = []
    for i in range(len(list)):
        list_pop.append(list[i]['pop'])
    for i in range(len(list_pop)):
        list_pop[i] *= 100
    print(f"Presipitasi : {list_pop[n]} %")
listPrecipitation(2)