import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

model1 = pickle.load(open('SW.pkl', 'rb'))
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict') # rendering the html template
def index() :
    return render_template('predict.html')

@app.route('/data_predict', methods=['GET','POST'])
def predict() :

    brand = request.form['Brand']
    if brand == 'Garmin':
        brand = 8
    if brand == 'Mobvoi':
        brand = 18
    if brand == 'Fitbit':
        brand = 6
    if brand == 'Fossil':
        brand = 7
    if brand == 'Amazfit':
        brand = 0
    if brand == 'Samsung':
        brand = 30
    if brand == 'Huawei':
        brand = 10
    if brand == 'Ticwatch':
        brand = 35
    if brand == 'Xiaomi':
        brand = 39
    if brand == 'Skagen':
        brand = 31
    if brand == 'Suunto':
        brand = 33
    if brand == 'Honor':
        brand = 9
    if brand == 'Apple':
        brand = 1
    if brand == 'Polar':
        brand = 27
    if brand == 'Casio':
        brand = 3
    if brand == 'Withings':
        brand = 38
    if brand == 'Oppo':
        brand = 26
    if brand == 'Timex':
        brand = 37
    if brand == 'Diesel':
        brand = 4
    if brand == 'Misfit':
        brand = 17
    if brand == 'LG':
        brand = 13
    if brand == 'Zepp':
        brand = 41
    if brand == 'Michael Kors':
        brand = 16
    if brand == 'TAG Heuer':
        brand = 34
    if brand == 'Asus':
        brand = 2

    model = request.form['Model']
    if model == 'Sense':
        model = 81
    if model == 'Falster 3':
        model = 22
    if model == 'Sport':
        model = 84
    if model == 'Watch GT 2 Pro':
        model = 121
    if model == 'TicWatch E3':
        model = 94
    if model == 'Forerunner 945':
        model = 24
    if model == 'Mi Watch Revolve':
        model = 62
    if model == '9 Peak':
        model = 2
    if model == '7':
        model = 0
    if model == 'Galaxy Watch 3':
        model = 35
    if model == 'Watch SE':
        model = 125
    if model == 'ScanWatch':
        model = 79
    if model == 'Pro 3':
        model = 71
    if model == 'GTR 2':
        model = 29
    if model == 'Watch GS Pro':
        model = 119
    if model == 'GTR 2e':
        model = 30
    if model == 'Watch Series 6':
        model = 126
    if model == 'Vantage V2':
        model = 102
    if model == 'Hybrid HR':
        model = 44
    if model == 'Venu Sq':
        model = 106
    if model == 'MagicWatch 2':
        model = 56
    if model == 'TicWatch Pro 3':
        model = 97
    if model == 'Vapor X':
        model = 104
    if model == 'Z':
        model = 132

    os = request.form['Operating System']
    if os == 'Wear OS':
        os = 31
    if os == 'Garmin OS':
        os = 9
    if os == 'Lite OS':
        os = 12
    if os == 'Fitbit OS':
        os = 7
    if os == 'Amazfit OS':
        os = 0
    if os == 'watchOS':
        os = 34
    if os == 'Tizen OS':
        os = 30
    if os == 'Proprietary OS':
        os = 23
    if os == 'Polar OS':
        os = 21
    if os == 'Proprietary':
        os = 22
    if os == 'Suunto OS':
        os = 27
    if os == 'Android Wear':
        os = 3
    if os == 'ColorOS':
        os = 5
    if os == 'Withings OS':
        os = 32
    if os == 'Zepp OS':
        os = 33
    if os == 'Casio OS':
        os = 4
    if os == 'Timex OS':
        os = 28
    if os == 'LiteOS':
        os = 13
    if os == 'Tizen':
        os = 29
    if os == 'HarmonyOS':
        os = 10
    if os == 'Custom OS':
        os = 6
    if os == 'Fossil OS':
        os = 8
    if os == 'Android OS':
        os = 2

    connect = request.form['Connectivity']
    if connect == 'Bluetooth, Wi-Fi':
        connect = 1
    if connect == 'Bluetooth, Wi-Fi, Cellular':
        connect = 2
    if connect == 'Bluetooth':
        connect = 0
    if connect == 'Bluetooth, Wi-Fi, GPS':
        connect = 3
    if connect == 'Bluetooth, Wi-Fi, NFC':
        connect = 4

    display_type = request.form['Display Type']
    if display_type == 'AMOLED':
        display_type = 0
    if display_type == 'LCD':
        display_type = 9
    if display_type == 'Transflective':
        display_type = 25
    if display_type == 'Super AMOLED':
        display_type = 21
    if display_type == 'OLED':
        display_type = 14
    if display_type == 'Retina':
        display_type = 17
    if display_type == 'IPS LCD':
        display_type = 8
    if display_type == 'TFT LCD':
        display_type = 23
    if display_type == 'PMOLED':
        display_type = 16
    if display_type == 'E-Ink':
        display_type = 4
    if display_type == 'Monochrome':
        display_type = 13
    if display_type == 'Sunlight-visible, transflective memory-in-pixel (MIP)':
        display_type = 20
    if display_type == 'P-OLED':
        display_type = 15
    if display_type == 'MIP':
        display_type = 10
    if display_type == 'IPS':
        display_type = 7

    display_size = float(request.form['Display Size'])

    resolution = request.form['Resolution']
    if resolution == '454 x 454':
        resolution = 32
    if resolution == '360 x 360':
        resolution = 22
    if resolution == '240 x 240':
        resolution = 8
    if resolution == '390 x 390':
        resolution = 25
    if resolution == '416 x 416':
        resolution = 30
    if resolution == '400 x 400':
        resolution = 28
    if resolution == '336 x 336':
        resolution = 19
    if resolution == '328 x 328':
        resolution = 18
    if resolution == '368 x 448':
        resolution = 23
    if resolution == '320 x 320':
        resolution = 15
    if resolution == '280 x 280':
        resolution = 10
    if resolution == '348 x 442':
        resolution = 21
    if resolution == '372 x 430':
        resolution = 24
    if resolution == '480 x 480':
        resolution = 34
    if resolution == '128 x 128':
        resolution = 1
    if resolution == '176 x 176':
        resolution = 3
    if resolution == '320 x 300':
        resolution = 13
    if resolution == '348 x 250':
        resolution = 20
    if resolution == '324 x 394':
        resolution = 16
    if resolution == '280 x 456':
        resolution = 12

    water = float(request.form['Water Resistance'])

    battery = float(request.form['Battery Life'])

    gps = request.form['GPS']
    if gps == 'Yes':
        gps = 1
    if gps == 'No':
        gps = 0

    nfc = request.form['NFC']
    if nfc == 'Yes':
        nfc = 1
    if nfc == 'No':
        nfc = 0

    prediction = model1.predict(pd.DataFrame([[brand,model,os,connect,display_type,display_size,resolution,water,battery,gps,nfc]],
                                             columns= ['Brand', 'Model', 'Operating System', 'Connectivity',
                                                        'Display Type', 'Display Size', 'Resolution',
                                                          'Water Resistance','Battery Life','GPS','NFC']))


    
    prediction = np.round(prediction,2)
    
    
    return render_template('watch_prediction.html', prediction_text ="is {}".format(prediction))



if __name__ == '__main__':
    app.run()