from pathlib import Path
from tkinter import *
import requests
from time import strftime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_change_text():
    canvas.itemconfig(cuaca_sekarang, text=(f"{weather}"))
    canvas.itemconfig(temperatur_sekarang, text=(f"{temperature}",chr(176),"C"))
    canvas.itemconfig(tekanan_sekarang, text=(f"{pressure} Pa"))
    canvas.itemconfig(kelembaban_sekarang, text=(f"{humidity}","%"))
def on_change_text2():
    canvas.itemconfig(cuaca_sekarang, text=" ")
    canvas.itemconfig(temperatur_sekarang, text=" ")
    canvas.itemconfig(tekanan_sekarang, text=" ")
    canvas.itemconfig(kelembaban_sekarang, text=" ")

def hpusMarkError():
    canvas.itemconfig(itk, text=" ")
    canvas.itemconfig(copyright, text=" ")
    canvas.itemconfig(notfound0, text =" ")
    canvas.itemconfig(notfound1, text=" ")
    canvas.itemconfig(notfound2, text=" ")
    canvas.itemconfig(notfound3, text=" " )




API_KEY = "d485793245775bad0112e296db963d3a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# fungsi tombol search
def mintaReq():
    global request_url,response,weather,weatherIcon,temperature,pressure,humidity
    global cuaca_sekarang, temperatur_sekarang, tekanan_sekarang, kelembaban_sekarang,image_27,copyright,itk,notfound0,notfound1,notfound2,notfound3
    try:
        hpusMarkError()
    except NameError:
        print("Baru Mulai Programnya Gan")
    try:
        on_change_text2()
    except NameError:
        print("Engine Startttt!!!!")
    try:
        canvas.delete(image_27)
    except:
        print("Nanti Pasang Kalau salah")
    print(f"{inputKota()}")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={inputKota()}&lang=en"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].title()
        weatherIcon = data['weather'][0]['icon']
        temperature = round(data["main"]["temp"] - 273.15, 1)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        # bagian cuaca saat ini
        cuaca_sekarang = canvas.create_text(
        668.7307739257812,
        133.11007690429688,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 19 * -1)
        )

    #temperatur hari ini
        temperatur_sekarang = canvas.create_text(
        668.7307739257812,
        205.95054626464844,
        anchor="nw",
        fill="#FFFFFF",
        text=" ",
        font=("Questrial Regular", 19 * -1)
        )

    #tekanan hari ini
        tekanan_sekarang = canvas.create_text(
        668.7307739257812,
        287,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 19 * -1)
        )

    #kelembaban hari ini

        kelembaban_sekarang = canvas.create_text(
        668.7307739257812,
        364,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 19 * -1)
        )
        on_change_text()
        def iconUtama():
            global image_image_16
            global image_16
            if (weatherIcon == "01d"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("cerah_banget.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "01n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("bulan.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "02d"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("cerah_berawan.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "02n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("BerawanMalam.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "03d" or weatherIcon == "03n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("berawan.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "04d" or weatherIcon == "04n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("mendung.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "11d" or weatherIcon == "11n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("bepetir.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "13d" or weatherIcon == "13n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("salju.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )

            elif (weatherIcon == "50d" or weatherIcon == "50n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("berangin.png"))
                image_16 = canvas.create_image(
                    629.358642578125,
                    134.6696319580078,
                    image=image_image_16
                )
        iconUtama()
        hpusMarkError()

        print("Wheather Icon : ", weatherIcon)
    if response.status_code == 404:
        print(f"Kota tidak ditemukan")
        image_27 = canvas.create_image(
            729.0,
            214.0,
            image=image_image_27
        )
        itk = canvas.create_text(
        637.1785888671875,
        404.8560485839844,
        anchor="nw",
        text="Institute of Technology Kalimantan, Indonesia",
        fill="#FFFFFF",
        font=("Questrial Regular", 9 * -1)
        )

        copyright = canvas.create_text(
        668.5232543945312,
        417.3939514160156,
        anchor="nw",
        text="©Copyright all rights reserved",
        fill="#FFFFFF",
        font=("Questrial Regular", 9 * -1)
        )

        notfound0 =canvas.create_text(
            733.0,
            290,
            anchor="center",
            text="Check your",
            fill="#FFFFFF",
            font=("Montserrat", 20 * -1)
        )

        notfound1 =canvas.create_text(
            733.0,
            310,
            anchor="center",
            text="typing or try again.",
            fill="#FFFFFF",
            font=("Montserrat", 20 * -1)
        )

        notfound2 =canvas.create_text(
            733.0,
            151.0,
            #ini center biar relatif sesuai panjang nama kota nya perataannya
            anchor="center",
            text=f"{inputKota()}",
            fill="#FFFFFF",
            font=("Open Sans Extrabold", 20 * -1)
        )

        notfound3 = canvas.create_text(
            733.0,
            173,
            anchor="center",
            text= "has not found",
            fill="#FFFFFF",
            font=("Montserrat", 20 * -1)
        )

        tombol()


window = Tk()

window.geometry("890x435")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 442,
    width = 890,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    287.0,
    124.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    78.76211547851562,
    140.95008850097656,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    293.54058837890625,
    140.95008850097656,
    image=image_image_3
)

image_image_oren = PhotoImage(
    file=relative_to_assets("orenoren.png"))
image_oren = canvas.create_image(
    120,
    226,
    image=image_image_oren
)

canvas.create_text(
    50.94380187988281,
    75.63072204589844,
    anchor="nw",
    text="06.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 25 * -1)
)

canvas.create_text(
    158.3330078125,
    75.63072204589844,
    anchor="nw",
    text="09.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 25 * -1)
)

canvas.create_text(
    262.3130187988281,
    75.63072204589844,
    anchor="nw",
    text="12.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 25 * -1)
)

canvas.create_text(
    369.7022705078125,
    75.63072204589844,
    anchor="nw",
    text="15.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 25 * -1)
)

canvas.create_text(
    468.56854248046875,
    75.63072204589844,
    anchor="nw",
    text="18.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 25 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    189.62841796875,
    140.35926055908203,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    396.4068603515625,
    142.95008850097656,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    496.9777526855469,
    139.54090881347656,
    image=image_image_6
)

canvas.create_text(
    50.94380187988281,
    176.2015838623047,
    anchor="nw",
    text="30°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    160.03758239746094,
    176.2015838623047,
    anchor="nw",
    text="29°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    264.0176086425781,
    176.2015838623047,
    anchor="nw",
    text="30°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    373.1114501953125,
    176.2015838623047,
    anchor="nw",
    text="27°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    468.56854248046875,
    176.2015838623047,
    anchor="nw",
    text="26°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    287.0,
    345.40501403808594,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    73.95585632324219,
    330.1938781738281,
    image=image_image_8
)

canvas.create_text(
    51.24757385253906,
    264.779296875,
    anchor="nw",
    text="Sun",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    162.2840576171875,
    264.779296875,
    anchor="nw",
    text="Mon",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    268.19580078125,
    264.779296875,
    anchor="nw",
    text="Tue",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    367.27447509765625,
    264.779296875,
    anchor="nw",
    text="Wed",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    466.3531799316406,
    264.779296875,
    anchor="nw",
    text="Thur",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    185.03456115722656,
    329.6103820800781,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    392.27447509765625,
    332.1938781738281,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    286.3627624511719,
    332.1938781738281,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    493.06146240234375,
    328.7773132324219,
    image=image_image_12
)

canvas.create_text(
    46.12281799316406,
    365.56622314453125,
    anchor="nw",
    text="30°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    155.4510498046875,
    365.56622314453125,
    anchor="nw",
    text="27°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    368.9827575683594,
    365.56622314453125,
    anchor="nw",
    text="27°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    263.071044921875,
    365.56622314453125,
    anchor="nw",
    text="26°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

canvas.create_text(
    464.6449279785156,
    365.56622314453125,
    anchor="nw",
    text="25°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 27 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    768.7140197753906,
    30.74854278564453,
    image=entry_image_1
)

def inputKota():
    input_kota = var.get()
    return input_kota

def temp_text(e):
   entry_1.delete(0,"end")

var = StringVar()

entry_1 = Entry(
    bd=0,
    bg="#9CBCD0",
    justify="left",
    font=("Questrial", 27 * -1),
    highlightthickness=0,
    textvariable = var
)

entry_1.insert(0, "TYPE YOUR CITY")
entry_1.bind("<FocusIn>", temp_text)

def autoupper(*arg):
    var.set(var.get().upper())

var.trace("w", autoupper)

entry_1.place(
    x=648,
    y=18,
    width=228.90594482421875,
    height=29
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mintaReq(),
    relief="flat"
)
button_1.place(
    x=583,
    y=9,
    width=42,
    height=40,
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    732.681396484375,
    221.0,
    image=image_image_13
)


canvas.create_text(
    71.74665832519531,
    0.0,
    anchor="nw",
    text="WEATHER FORECAST",
    fill="#FF6700",
    font=("Open Sans Extrabold", 42 * -1)
)


canvas.create_text(
    669.2031860351562,
    182.75608825683594,
    anchor="nw",
    text="TEMPERATURE",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

canvas.create_text(
    669.2031860351562,
    260.02398681640625,
    anchor="nw",
    text="AIR PRESSURE",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    630.2061157226562,
    287.6001281738281,
    image=image_image_14
)

canvas.create_text(
    668.7307739257812,
    107.54867553710938,
    anchor="nw",
    text="WEATHER NOW",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

canvas.create_text(
    669.2031860351562,
    338,
    anchor="nw",
    text="HUMIDITY",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    630.2569580078125,
    355.6671142578125,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    629.358642578125,
    134.6696319580078,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    629.053466796875,
    209.7366180419922,
    image=image_image_17
)

def hapusWaktu():
    canvas.itemconfig(mesinWaktu, text=" ")
def addWaktu():
    canvas.itemconfig(mesinWaktu, text= string)

def time():
    global mesinWaktu,string
    try :
        hapusWaktu()
    except :
        print("Mesin Waktu Dimulai")
    string = strftime('%A : %D : %r')
    mesinWaktu = canvas.create_text(730, 75, text= string, font=("Open Sans Regular", 16 * -1), fill="#FFFFFF", anchor="center")
    canvas.after(1000, time)
    addWaktu()
time()

canvas.create_text(
    668.5232543945312,
    417.3939514160156,
    anchor="nw",
    text="©Copyright all rights reserved",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

canvas.create_text(
    637.1785888671875,
    404.8560485839844,
    anchor="nw",
    text="Institute of Technology Kalimantan, Indonesia",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

canvas.create_text(
    668.5232543945312,
    417.3939514160156,
    anchor="nw",
    text="©Copyright all rights reserved",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

canvas.create_text(
    637.1785888671875,
    404.8560485839844,
    anchor="nw",
    text="Institute of Technology Kalimantan, Indonesia",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

image_image_oren2 = PhotoImage(
    file=relative_to_assets("orenoren.png"))
image_oren2 = canvas.create_image(
    120,
    420,
    image=image_image_oren2
)


canvas.create_text(
    25,
    214,
    anchor="nw",
    text="WEATHER TODAY",
    fill="#FFFFFF",
    font=("Open Sans Bold", 18 * -1)
)

canvas.create_text(
    25,
    409,
    anchor="nw",
    text="THE NEXT FEW DAYS",
    fill="#FFFFFF",
    font=("Open Sans Bold", 18 * -1)
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))

window.resizable(False, False)
window.mainloop()
