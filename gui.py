import sys
import os
from pathlib import Path
from tkinter import *
import requests
from datetime import datetime, timedelta
from time import strftime


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tombol():
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: restart_program(),
        relief="flat"
    )
    button_2.place(
        x=343.0,
        y=4.0,
        width=23.0,
        height=22.0
    )

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

API_KEY = "d485793245775bad0112e296db963d3a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# fungsi tombol search
def mintaReq():
    print(f"{inputKota()}")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={inputKota()}&lang=id"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].title()
        weatherIcon = data['weather'][0]['icon']
        temperature = round(data["main"]["temp"] - 273.15, 1)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        # bagian cuaca saat ini
        def cuacaUtama():
            canvas.create_text(
                386.48321533203125,
                66.05583190917969,
                anchor="nw",
                text=f"{weather}",
                fill="#FFFFFF",
                font=("Questrial Regular", 12 * -1)
            )
        cuacaUtama()

        #temperatur hari ini
        def temperatureUtama():
            canvas.create_text(
                            386.48321533203125,
                            115.02796173095703,
                            anchor="nw",
                            fill="#FFFFFF",
                            text=(f"{temperature}",chr(176),"C"),
                            font=("Questrial Regular", 12 * -1)
                            )

        temperatureUtama()
        #tekanan hari ini
        def pressureUtama():
            canvas.create_text(
                386.48321533203125,
                164.00009155273438,
                anchor="nw",
                text=f"{pressure}",
                fill="#FFFFFF",
                font=("Questrial Regular", 12 * -1)
            )

        pressureUtama()
        #kelembaban hari ini
        def humidityUtama():
            canvas.create_text(
                386.48321533203125,
                212.97225952148438,
                anchor="nw",
                text=(f"{humidity}","%"),
                fill="#FFFFFF",
                font=("Questrial Regular", 12 * -1)
            )

        humidityUtama()
        tombol()

        def iconUtama():
            global image_image_16
            global image_16
            if (weatherIcon == "01d"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("cerah_banget.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "01n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("bulan.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "02d"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("cerah_berawan.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "02n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("BerawanMalam.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "03d" or weatherIcon == "03n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("berawan.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "04d" or weatherIcon == "04n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("mendung.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "11d" or weatherIcon == "11n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("bepetir.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "13d" or weatherIcon == "13n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("salju.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )

            elif (weatherIcon == "50d" or weatherIcon == "50n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("berangin.png"))
                image_16 = canvas.create_image(
                    361.3055114746094,
                    66.58848571777344,
                    image=image_image_16
                )
        iconUtama()

        print("Wheather Icon : ", weatherIcon)
    if response.status_code == 404:
        print(f"Kota tidak ditemukan")

        image_27 = canvas.create_image(
            427.0,
            125.0,
            image=image_image_27
        )

        canvas.create_text(
            391.3489685058594,
            244.339599609375,
            anchor="nw",
            text="©Copyright all rights reserved",
            fill="#FFFFFF",
            font=("Questrial Regular", 5 * -1)
        )

        canvas.create_text(
            373.0,
            237.0,
            anchor="nw",
            text="Institute of Technology Kalimantan, Indonesia",
            fill="#FFFFFF",
            font=("Questrial Regular", 5 * -1)
        )

        canvas.create_text(
            373.0,
            154.0,
            anchor="nw",
            text="typing or try again.",
            fill="#FFFFFF",
            font=("Montserrat", 11 * -1)
        )

        canvas.create_text(
            395.0,
            141.0,
            anchor="nw",
            text="Check your",
            fill="#FFFFFF",
            font=("Montserrat", 11 * -1)
        )

        canvas.create_text(
            428.0,
            72.0,
            #ini center biar relatif sesuai panjang nama kota nya perataannya
            anchor="center",
            text=f"{inputKota()}",
            fill="#FFFFFF",
            font=("Open Sans Extrabold", 11 * -1)
        )


        canvas.create_text(
            388.0,
            78.0,
            anchor="nw",
            text= "has not found",
            fill="#FFFFFF",
            font=("Montserrat", 11 * -1)
        )

        tombol()



window = Tk()

window.geometry("521x254")
window.configure(bg = "#FFFFFF")
window.title('WHEATHER FORECAST')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 259,
    width = 521,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    170.0,
    73.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    43.0,
    83.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    169.0,
    83.0,
    image=image_image_3
)

canvas.create_text(
    27.0,
    45.0,
    anchor="nw",
    text="06.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 15 * -1)
)

canvas.create_text(
    90.0,
    45.0,
    anchor="nw",
    text="09.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 15 * -1)
)

canvas.create_text(
    151.0,
    45.0,
    anchor="nw",
    text="12.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 15 * -1)
)

canvas.create_text(
    214.0,
    45.0,
    anchor="nw",
    text="15.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 15 * -1)
)


canvas.create_text(
    272.0,
    45.0,
    anchor="nw",
    text="18.00",
    fill="#FFFFFF",
    font=("JostRoman Regular", 15 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    108.0,
    83.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    230.0,
    84.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    288.0,
    82.0,
    image=image_image_6
)

canvas.create_text(
    27.0,
    104.0,
    anchor="nw",
    text="30°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    91.0,
    104.0,
    anchor="nw",
    text="29°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    152.0,
    104.0,
    anchor="nw",
    text="30°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    216.0,
    104.0,
    anchor="nw",
    text="27°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    272.0,
    104.0,
    anchor="nw",
    text="26°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    168.0,
    202.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    43.0,
    193.0,
    image=image_image_8
)

canvas.create_text(
    30.0,
    155.0,
    anchor="nw",
    text="Sun",
    fill="#FFFFFF",
    font=("JostRoman Regular", 17 * -1)
)

canvas.create_text(
    95.0,
    155.0,
    anchor="nw",
    text="Mon",
    fill="#FFFFFF",
    font=("JostRoman Regular", 17 * -1)
)

canvas.create_text(
    157.0,
    155.0,
    anchor="nw",
    text="Tue",
    fill="#FFFFFF",
    font=("JostRoman Regular", 17 * -1)
)

canvas.create_text(
    215.0,
    155.0,
    anchor="nw",
    text="Wed",
    fill="#FFFFFF",
    font=("JostRoman Regular", 17 * -1)
)

canvas.create_text(
    273.0,
    155.0,
    anchor="nw",
    text="Thur",
    fill="#FFFFFF",
    font=("JostRoman Regular", 17 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    108.0,
    193.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    230.0,
    194.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    168.0,
    194.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    288.0,
    192.0,
    image=image_image_12
)

canvas.create_text(
    27.0,
    214.0,
    anchor="nw",
    text="30°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    15.0,
    239.0,
    anchor="nw",
    text="THE NEXT FEW DAYS",
    fill="#FFFFFF",
    font=("OpenSans Bold", 11 * -1)
)

canvas.create_text(
    91.0,
    214.0,
    anchor="nw",
    text="27°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    216.0,
    214.0,
    anchor="nw",
    text="27°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    154.0,
    214.0,
    anchor="nw",
    text="26°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    272.0,
    214.0,
    anchor="nw",
    text="25°C",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

#OS MACBOOK AND LINUX TRANSPARENT
#window.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
#window.config(bg='systemTransparent')

#OS WINDOWS TRANSPARENT
#window.wm_attributes('-transparentcolor', '#ab23ff')
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(window,font=("OpenSans Bold", 9), bg='#FF6700', fg="white", anchor="center")
mark.place(x=60.0, y=124.0)
time()

#hari ini, jam sekarang
updated = ( datetime.now() +
           timedelta()).strftime('%A, %H:%M:%S')
canvas.create_text(
    13.0,
    126.0,
    anchor="nw",
    text=(updated),
    fill="#FFFFFF",
    font=("OpenSans Bold", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    450.0,
    18.0,
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
    font=("Montserrat", 18 * -1),
    highlightthickness=0,
    textvariable = var
)

entry_1.insert(0, "TYPE PLACES")
entry_1.bind("<FocusIn>", temp_text)

def autoupper(*arg):
    var.set(var.get().upper())

var.trace("w", autoupper)

entry_1.place(
    x=378.0,
    y=7.0,
    width=134.0,
    height=21.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

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
    x=343.0,
    y=4.0,
    width=23.0,
    height=22.0
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    429.0,
    129.0,
    image=image_image_13
)

canvas.create_text(
    381.0,
    12.0,
    anchor="nw",
    text="TYPE YOUR CITY",
    fill="#FFFFFF",
    font=("Questrial Regular", 16 * -1)
)

canvas.create_text(
    42.0,
    0.0,
    anchor="nw",
    text="WEATHER FORECAST",
    fill="#FF6700",
    font=("Open Sans Extrabold", 25 * -1)
)

canvas.create_text(
    386.7799072265625,
    97.23987579345703,
    anchor="nw",
    text="TEMPERATURE",
    fill="#FF6700",
    font=("Montserrat", 12 * -1)
)

canvas.create_text(
    386.7799072265625,
    145.77398681640625,
    anchor="nw",
    text="AIR PRESSURE",
    fill="#FF6700",
    font=("Montserrat", 12 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    361.9784240722656,
    162.5327606201172,
    image=image_image_14
)

canvas.create_text(
    386.48321533203125,
    50.0,
    anchor="nw",
    text="WEATHER NOW",
    fill="#FF6700",
    font=("Montserrat", 12 * -1)
)

canvas.create_text(
    386.7799072265625,
    197.54371643066406,
    anchor="nw",
    text="HUMIDITY",
    fill="#FF6700",
    font=("Montserrat", 12 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    361.7541198730469,
    206.05630493164062,
    image=image_image_15
)


image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    361.3055114746094,
    66.58848571777344,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    361.6513366699219,
    114.11202239990234,
    image=image_image_17
)

canvas.create_text(
    391.3489685058594,
    244.339599609375,
    anchor="nw",
    text="©Copyright all rights reserved",
    fill="#FFFFFF",
    font=("Questrial Regular", 5 * -1)
)

canvas.create_text(
    373.0,
    237.0,
    anchor="nw",
    text="Institute of Technology Kalimantan, Indonesia",
    fill="#FFFFFF",
    font=("Questrial Regular", 5 * -1)
)

image_image_27 = PhotoImage(
    file=relative_to_assets("ImageNotFound.png"))

window.resizable(False, False)
window.mainloop()
