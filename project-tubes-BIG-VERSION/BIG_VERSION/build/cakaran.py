from pathlib import Path
from tkinter import *
import requests
from time import strftime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    text="anjay",
    fill="#FFFFFF",
    font=("JostRoman Regular", 25 * -1)
)

window.resizable(False, False)
window.mainloop()