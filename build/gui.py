import pandas as pd

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import END, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage

from train import train_model, predict_aqi_category, predict_aqi_category_auto

# Load the dataset
data = pd.read_csv("globalAirPollutionDataset.csv")

# Train the model and get the label encoder
model, lbl_encoder = train_model(data=data)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Documents\Data_Analytics_Project\GUI\build\assets\frame0") # This path should be changed to your own 'frame0' path.


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x684")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 684,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    684.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    106.0,
    fill="#16009F",
    outline="")

canvas.create_rectangle(
    34.0,
    111.0,
    764.0,
    445.0,
    fill="#E6E6E6",
    outline="")

canvas.create_text(
    41.0,
    122.0,
    anchor="nw",
    text="AQI\nCategory",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    57.0,
    452.0,
    anchor="nw",
    text="* CO in mg/m3 and other pollutants in μg/m3; 2-hourly average values for for PM10, PM2.5, NO2, SO2, \nNH3, and Pb, and 8-hourly values for CO and O3.",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    34.0,
    491.0,
    anchor="nw",
    text="CO AQI Value",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    158.0,
    491.0,
    anchor="nw",
    text="(0 - 200)",
    fill="#424242",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    612.0,
    551.0,
    anchor="nw",
    text="Predicted Category",
    fill="#4F4F4F",
    font=("TimesNewRomanPS BoldMT", 12 * -1)
)

canvas.create_text(
    158.0,
    539.0,
    anchor="nw",
    text="(0 - 300)",
    fill="#424242",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    158.0,
    587.0,
    anchor="nw",
    text="(0 - 100)",
    fill="#424242",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    158.0,
    635.0,
    anchor="nw",
    text="(0 - 500)",
    fill="#424242",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    34.0,
    539.0,
    anchor="nw",
    text="O3 AQI Value",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    34.0,
    588.0,
    anchor="nw",
    text="NO2 AQI Value",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_rectangle(
    423.0,
    510.0,
    487.0274076613314,
    583.9769879320911,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    423.0,
    582.9769924214997,
    487.0274085898127,
    655.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    423.0,
    582.9999998993198,
    487.0000018400201,
    607.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    423.0,
    558.0,
    485.99999913622105,
    583.9999993303629,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    591.0,
    583.0,
    612.0,
    584.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_clicked(),
    relief="flat"
)
button_1.place(
    x=487.0,
    y=567.0,
    width=115.0,
    height=40.0
)

canvas.create_text(
    34.0,
    636.0,
    anchor="nw",
    text="PM2.5 AQI Value",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 16 * -1)
)

canvas.create_text(
    136.0,
    122.0,
    anchor="nw",
    text="AQI",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    206.0,
    122.0,
    anchor="nw",
    text="Concentration Range",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_rectangle(
    34.0,
    205.0,
    764.0,
    245.0,
    fill="#17A700",
    outline="")

canvas.create_rectangle(
    34.0,
    245.0,
    764.0,
    285.0,
    fill="#95C900",
    outline="")

canvas.create_rectangle(
    34.0,
    285.0,
    764.0,
    325.0,
    fill="#DDD400",
    outline="")

canvas.create_rectangle(
    34.0,
    325.0,
    764.0,
    365.0,
    fill="#D49900",
    outline="")

canvas.create_rectangle(
    34.0,
    365.0,
    764.0,
    405.0,
    fill="#E95400",
    outline="")

canvas.create_rectangle(
    34.0,
    405.0,
    764.0,
    445.0,
    fill="#A70A00",
    outline="")

canvas.create_rectangle(
    33.0,
    164.0,
    764.0,
    165.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    244.0,
    764.0,
    245.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    695.0,
    164.0,
    696.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    625.0,
    164.0,
    626.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    555.0,
    164.0,
    556.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    485.5,
    163.99911499023438,
    486.50000000000006,
    445.00091552734375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    415.0,
    164.0,
    416.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    345.0,
    164.0,
    346.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    275.0,
    164.0,
    276.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    205.0,
    110.0,
    206.00000000000003,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    135.0,
    110.0,
    136.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    284.0,
    764.0,
    285.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    324.0,
    764.0,
    325.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    364.0,
    764.0,
    365.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    404.0,
    764.0,
    405.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    444.0,
    764.0,
    445.0,
    fill="#000000",
    outline="")

canvas.create_text(
    41.0,
    205.0,
    anchor="nw",
    text="Good",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    41.0,
    245.0,
    anchor="nw",
    text="Satisfactory",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    41.0,
    285.0,
    anchor="nw",
    text="Moderately \npolluted",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    41.0,
    325.0,
    anchor="nw",
    text="Poor",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    41.0,
    365.0,
    anchor="nw",
    text="Very poor",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    41.0,
    405.0,
    anchor="nw",
    text="Severe",
    fill="#000000",
    font=("TimesNewRomanPS BoldMT", 14 * -1)
)

canvas.create_text(
    136.0,
    205.0,
    anchor="nw",
    text="0 - 50",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    205.0,
    anchor="nw",
    text="0 - 50",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    165.0,
    anchor="nw",
    text="PM10",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    165.0,
    anchor="nw",
    text="PM2.5",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    165.0,
    anchor="nw",
    text="NO2",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    165.0,
    anchor="nw",
    text="O3",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    165.0,
    anchor="nw",
    text="CO",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    165.0,
    anchor="nw",
    text="SO2",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    165.0,
    anchor="nw",
    text="NH3",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    165.0,
    anchor="nw",
    text="Pb",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    205.0,
    anchor="nw",
    text="0 - 30",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    205.0,
    anchor="nw",
    text="0 - 40",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    205.0,
    anchor="nw",
    text="0 - 50",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    205.0,
    anchor="nw",
    text="0 - 1.0",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    205.0,
    anchor="nw",
    text="0 - 40",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    205.0,
    anchor="nw",
    text="0 - 200",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    205.0,
    anchor="nw",
    text="0 - 0.5",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    136.0,
    245.0,
    anchor="nw",
    text="51 - 100",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    245.0,
    anchor="nw",
    text="51 - 100",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    245.0,
    anchor="nw",
    text="31 - 60",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    245.0,
    anchor="nw",
    text="41 - 80",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    245.0,
    anchor="nw",
    text="51 -100",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    245.0,
    anchor="nw",
    text="1.1 - 2.0",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    245.0,
    anchor="nw",
    text="41 - 80",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    245.0,
    anchor="nw",
    text="201 - 400",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    245.0,
    anchor="nw",
    text="0.5 - 1.0",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    136.0,
    285.0,
    anchor="nw",
    text="101 - 200",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    285.0,
    anchor="nw",
    text="101 - 250",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    285.0,
    anchor="nw",
    text="61 - 90",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    285.0,
    anchor="nw",
    text="81 - 180",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    285.0,
    anchor="nw",
    text="101 - 168",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    285.0,
    anchor="nw",
    text="2.1 - 10",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    285.0,
    anchor="nw",
    text="81 - 380",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    285.0,
    anchor="nw",
    text="401 - 800",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    285.0,
    anchor="nw",
    text="1.1 - 2.0",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    136.0,
    325.0,
    anchor="nw",
    text="201 - 300",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    325.0,
    anchor="nw",
    text="251 - 350",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    325.0,
    anchor="nw",
    text="91 - 120",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    325.0,
    anchor="nw",
    text="181 - 280",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    325.0,
    anchor="nw",
    text="169 - 208",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    325.0,
    anchor="nw",
    text="10 - 17",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    325.0,
    anchor="nw",
    text="381 - 800",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    325.0,
    anchor="nw",
    text="801 - 1200",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    325.0,
    anchor="nw",
    text="2.1 - 3.0",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    136.0,
    365.0,
    anchor="nw",
    text="301 - 400",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    365.0,
    anchor="nw",
    text="351 - 430",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    365.0,
    anchor="nw",
    text="121 - 250",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    365.0,
    anchor="nw",
    text="281 - 400",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    365.0,
    anchor="nw",
    text="209 - 748*",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    365.0,
    anchor="nw",
    text="17 - 34",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    365.0,
    anchor="nw",
    text="801 - 1600",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    365.0,
    anchor="nw",
    text="1200 -\n1800",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    365.0,
    anchor="nw",
    text="3.1 - 3.5",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    136.0,
    405.0,
    anchor="nw",
    text="401 - 500",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    206.0,
    405.0,
    anchor="nw",
    text="430+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    276.0,
    405.0,
    anchor="nw",
    text="250+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    346.0,
    405.0,
    anchor="nw",
    text="400+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    416.0,
    405.0,
    anchor="nw",
    text="748+*",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    486.0,
    405.0,
    anchor="nw",
    text="34+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    556.0,
    405.0,
    anchor="nw",
    text="1600+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    626.0,
    405.0,
    anchor="nw",
    text="1800+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

canvas.create_text(
    696.0,
    405.0,
    anchor="nw",
    text="3.5+",
    fill="#000000",
    font=("TimesNewRomanPSMT", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    325.0,
    511.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=236.0,
    y=497.0,
    width=178.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    695.0,
    584.0,
    image=entry_image_2
)
predict_str = StringVar()
predict_str.set('')
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=predict_str,
    state="disabled"
)
entry_2.place(
    x=622.0,
    y=570.0,
    width=146.0,
    height=26.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    325.0,
    559.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=236.0,
    y=545.0,
    width=178.0,
    height=26.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    325.0,
    607.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=236.0,
    y=593.0,
    width=178.0,
    height=26.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    325.0,
    655.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=236.0,
    y=641.0,
    width=178.0,
    height=26.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    399.0,
    53.0,
    image=image_image_1
)

canvas.create_text(
    166.0,
    29.0,
    anchor="nw",
    text="Air Pollution Detector",
    fill="#222222",
    font=("Inter ExtraBold", 42 * -1)
)

def button_clicked():
    print('===============================================')
    print("Prediction Result:-")
    print('===============================================')
    try:
        # Convert entry values to float
        co_aqi = float(entry_1.get())
        ozone_aqi = float(entry_3.get())
        no2_aqi = float(entry_4.get())
        pm25_aqi = float(entry_5.get())  
        
        co_aqi_category, ozone_aqi_category, no2_aqi_category, pm25_aqi_category = predict_aqi_category_auto(co_aqi, ozone_aqi, no2_aqi, pm25_aqi)
        # Make the prediction
        predicted_category = predict_aqi_category(model, lbl_encoder, co_aqi, co_aqi_category, ozone_aqi, ozone_aqi_category, no2_aqi, no2_aqi_category, pm25_aqi, pm25_aqi_category)

        # Display the result
        set_text(text=f'{predicted_category}')

        print('> %-18s : %s' % ('CO AQI Category', co_aqi_category))
        print('> %-18s : %s' % ('Ozone AQI Category', ozone_aqi_category))
        print('> %-18s : %s' % ('NO2 AQI Category', no2_aqi_category))
        print('> %-18s : %s' % ('PM2.5 AQI Category', pm25_aqi_category))
        print('===============================================')
        print('> %-18s : %s' % ('Predicted Category', predicted_category))
        print('===============================================')
        print('')

    except ValueError:
        # Handle the case where the user entered a non-numeric value
        set_text(text='Invalid numeric values.')

def set_text(text):
    predict_str.set(text)
    return

window.resizable(False, False)
window.mainloop()
