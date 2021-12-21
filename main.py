import json
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import urllib.request
from PIL import ImageTk, Image
import io
import time
class kakao():

    def login(self):
        URL = 'http://redcomet.duckdns.org/login'

        driver = webdriver.Chrome()
        driver.get(url=URL)

        try:
            element = WebDriverWait(driver, 60).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            output = json.loads(alert.text)
            token = output['token']
            nickname = output['nickname']
            image_url = output['image_url']

            alert.accept()
            driver.quit()

            kakao.token = token
            kakao.nickname = nickname
            kakao.image_url = image_url

        except:
            driver.quit()


class TK():

    def setSave(self):
        setDict = {'token': kakao.token,
                   'light_start_time': TK.ledTimeLowVar.get(),
                   'light_end_time': TK.ledTimeHighVar.get(),
                   'air_temp_low': TK.airTempLowVar.get(),
                   'air_temp_high': TK.airTempHighVar.get(),
                   'air_co2_low': TK.airCo2LowVar.get(),
                   'air_co2_high': TK.airCo2HighVar.get(),
                   'air_moisture_low': TK.airMoistureLowVar.get(),
                   'air_moisture_high': TK.airMoistureHighVar.get(),
                   'water_temp_low': TK.waterTempLowVar.get(),
                   'water_temp_high': TK.waterTempHighVar.get(),
                   'water_tds_low': TK.waterTdsLowVar.get(),
                   'water_tds_high': TK.waterTdsHighVar.get(),
                   'water_cycle': TK.waterCycleVar.get()}
        json_input = json.dumps(setDict)
        # print(json_output)
        json_output = cropData.setCropBase(self, data=json_input)
        if(json_output['result'] == 'ok'):
            tkinter.messagebox.showinfo("알림", "저장 완료")            
        else:
            tkinter.messagebox.showinfo("경고", "권한 없음")

    def makeSetting(self):
        TK.settingWindow = tkinter.Toplevel(TK.window)
        TK.settingWindow.iconbitmap('res/favicon.ico')

        setButton = tkinter.Button(
            TK.settingWindow, text="설정 저장")
        setButton.bind("<Button>", TK.setSave)
        setButton.grid(column=0, row=0, padx=5, pady=5)

        tkinter.Label(TK.settingWindow, text="최소").grid(
            column=1, row=0, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="최대").grid(
            column=2, row=0, padx=5, pady=5)

        TK.ledTimeLowVar = tkinter.StringVar()
        TK.ledTimeLowVar.set(cropData.jsonCropBase["light_start_time"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.ledTimeLowVar, width=10).grid(
            column=1, row=1, padx=5, pady=5)

        TK.ledTimeHighVar = tkinter.StringVar()
        TK.ledTimeHighVar.set(cropData.jsonCropBase["light_end_time"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.ledTimeHighVar, width=10).grid(
            column=2, row=1, padx=5, pady=5)

        TK.airTempLowVar = tkinter.StringVar()
        TK.airTempLowVar.set(cropData.jsonCropBase["air_temp_low"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.airTempLowVar, width=10).grid(
            column=1, row=2, padx=5, pady=5)

        TK.airTempHighVar = tkinter.StringVar()
        TK.airTempHighVar.set(cropData.jsonCropBase["air_temp_high"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.airTempHighVar, width=10).grid(
            column=2, row=2, padx=5, pady=5)

        TK.airCo2LowVar = tkinter.StringVar()
        TK.airCo2LowVar.set(cropData.jsonCropBase["air_co2_low"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.airCo2LowVar, width=10).grid(
            column=1, row=3, padx=5, pady=5)

        TK.airCo2HighVar = tkinter.StringVar()
        TK.airCo2HighVar.set(cropData.jsonCropBase["air_co2_high"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.airCo2HighVar, width=10).grid(
            column=2, row=3, padx=5, pady=5)

        TK.airMoistureLowVar = tkinter.StringVar()
        TK.airMoistureLowVar.set(cropData.jsonCropBase["air_moisture_low"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.airMoistureLowVar, width=10).grid(
            column=1, row=4, padx=5, pady=5)

        TK.airMoistureHighVar = tkinter.StringVar()
        TK.airMoistureHighVar.set(cropData.jsonCropBase["air_moisture_high"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.airMoistureHighVar, width=10).grid(
            column=2, row=4, padx=5, pady=5)

        TK.waterTempLowVar = tkinter.StringVar()
        TK.waterTempLowVar.set(cropData.jsonCropBase["water_temp_low"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.waterTempLowVar, width=10).grid(
            column=1, row=5, padx=5, pady=5)

        TK.waterTempHighVar = tkinter.StringVar()
        TK.waterTempHighVar.set(cropData.jsonCropBase["water_temp_high"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.waterTempHighVar, width=10).grid(
            column=2, row=5, padx=5, pady=5)

        TK.waterTdsLowVar = tkinter.StringVar()
        TK.waterTdsLowVar.set(cropData.jsonCropBase["water_tds_low"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.waterTdsLowVar, width=10).grid(
            column=1, row=6, padx=5, pady=5)

        TK.waterTdsHighVar = tkinter.StringVar()
        TK.waterTdsHighVar.set(cropData.jsonCropBase["water_tds_high"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.waterTdsHighVar, width=10).grid(
            column=2, row=6, padx=5, pady=5)

        TK.waterCycleVar = tkinter.StringVar()
        TK.waterCycleVar.set(cropData.jsonCropBase["water_cycle"])
        tkinter.Entry(TK.settingWindow, textvariable=TK.waterCycleVar, width=10).grid(
            column=1, row=7, padx=5, pady=5)

        tkinter.Label(TK.settingWindow, text="LED 시간").grid(
            column=0, row=1, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="공기 온도").grid(
            column=0, row=2, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="이산화탄소 농도").grid(
            column=0, row=3, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="습도").grid(
            column=0, row=4, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="물 온도").grid(
            column=0, row=5, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="TDS 농도").grid(
            column=0, row=6, padx=5, pady=5)
        tkinter.Label(TK.settingWindow, text="물 주기").grid(
            column=0, row=7, padx=5, pady=5)

    def refreshGallery(self, x):
        # print(TK.combobox.get())
        slot = TK.combobox.get()
        link = f'http://redcomet.duckdns.org/getCropImage{slot}.png'
        raw_data = urllib.request.urlopen(link).read()
        im = Image.open(io.BytesIO(raw_data))
        im = im.resize((200, 200))

        TK.galleryImageData = ImageTk.PhotoImage(im)
        TK.galleryImage = tkinter.Label(
            TK.galleryWindow, image=TK.galleryImageData, width=200, height=200)
        TK.galleryImage.grid(column=0, row=1, padx=5, pady=5)


    def makeGallery(self):
        TK.galleryWindow = tkinter.Toplevel(TK.window)
        TK.galleryWindow.iconbitmap('res/favicon.ico')
        slotList = [x for x in range(
            1, int(cropData.jsonCropBase['max_slot'])+1)]

        selected_slot = tkinter.StringVar()
        TK.combobox = tkinter.ttk.Combobox(
            TK.galleryWindow, textvariable=selected_slot)
        TK.combobox['values'] = slotList
        TK.combobox.grid(column=0, row=0, padx=5, pady=5)
        TK.combobox.bind("<<ComboboxSelected>>", TK().refreshGallery)
        TK.combobox.set(slotList[0])
        TK().refreshGallery(self)

    def makeSummary(self):
        
        cropData().getCropBase()
        cropData().getCropLog()
        
        newWindow = tkinter.Toplevel(TK.window)
        newWindow.iconbitmap('res/favicon.ico')

        TK.labelAirImage = Image.open("res/air.png")
        TK.labelAirImage = TK.labelAirImage.resize((50, 50), Image.ANTIALIAS)
        TK.labelAirImage = ImageTk.PhotoImage(TK.labelAirImage)
        AirImage = tkinter.Label(newWindow, image=TK.labelAirImage)
        AirImage.grid(column=0, row=0, padx=5, pady=5)

        TK.labelWaterImage = Image.open("res/water.png")
        TK.labelWaterImage = TK.labelWaterImage.resize(
            (50, 50), Image.ANTIALIAS)
        TK.labelWaterImage = ImageTk.PhotoImage(TK.labelWaterImage)
        WaterImage = tkinter.Label(newWindow, image=TK.labelWaterImage)
        WaterImage.grid(column=0, row=3, padx=5, pady=5)

        if(cropData.jsonCropLog['air_temp'] < cropData.jsonCropBase['air_temp_low'] or cropData.jsonCropLog['air_temp'] > cropData.jsonCropBase['air_temp_high']):
            TK.labelAirTemp = tkinter.Label(
                newWindow, text="공기 온도 : "+str(cropData.jsonCropLog['air_temp'])+"(비정상)", fg='red')
        else:
            TK.labelAirTemp = tkinter.Label(
                newWindow, text="공기 온도 : "+str(cropData.jsonCropLog['air_temp'])+"(정상)", fg='green')
        TK.labelAirTemp.grid(column=1, row=0, padx=5, pady=5)

        if(cropData.jsonCropLog['air_co2'] < cropData.jsonCropBase['air_co2_low'] or cropData.jsonCropLog['air_co2'] > cropData.jsonCropBase['air_co2_high']):
            TK.labelAirCo2 = tkinter.Label(
                newWindow, text="이산화탄소 농도 : "+str(cropData.jsonCropLog['air_co2'])+"(비정상)", fg='red')
        else:
            TK.labelAirCo2 = tkinter.Label(
                newWindow, text="이산화탄소 농도 : "+str(cropData.jsonCropLog['air_co2'])+"(정상)", fg='green')
        TK.labelAirCo2.grid(column=1, row=1, padx=5, pady=5)

        if(cropData.jsonCropLog['air_moisture'] < cropData.jsonCropBase['air_moisture_low'] or cropData.jsonCropLog['air_moisture'] > cropData.jsonCropBase['air_moisture_high']):
            TK.labelAirMoisture = tkinter.Label(
                newWindow, text="습도 : "+str(cropData.jsonCropLog['air_moisture'])+"(비정상)", fg='red')
        else:
            TK.labelAirMoisture = tkinter.Label(
                newWindow, text="습도 : "+str(cropData.jsonCropLog['air_moisture'])+"(정상)", fg='green')
        TK.labelAirMoisture.grid(column=1, row=2, padx=5, pady=5)

        if(cropData.jsonCropLog['water_temp'] < cropData.jsonCropBase['water_temp_low'] or cropData.jsonCropLog['water_temp'] > cropData.jsonCropBase['water_temp_high']):
            TK.labelWaterTemp = tkinter.Label(
                newWindow, text="물 온도 : "+str(cropData.jsonCropLog['water_temp'])+"(비정상)", fg='red')
        else:
            TK.labelWaterTemp = tkinter.Label(
                newWindow, text="물 온도 : "+str(cropData.jsonCropLog['water_temp'])+"(정상)", fg='green')
        TK.labelWaterTemp.grid(column=1, row=3, padx=5, pady=5)

        if(cropData.jsonCropLog['water_tds'] < cropData.jsonCropBase['water_tds_low'] or cropData.jsonCropLog['water_tds'] > cropData.jsonCropBase['water_tds_high']):
            TK.labelWaterTds = tkinter.Label(
                newWindow, text="TDS : "+str(cropData.jsonCropLog['water_tds'])+"(비정상)", fg='red')
        else:
            TK.labelWaterTds = tkinter.Label(
                newWindow, text="TDS : "+str(cropData.jsonCropLog['water_tds'])+"(정상)", fg='green')
        TK.labelWaterTds.grid(column=1, row=4, padx=5, pady=5)

    def makeGraph(self):

        cropData().getCropBase()
        cropData().getCropLogs()
        
        newWindow = tkinter.Toplevel(TK.window)
        newWindow.iconbitmap('res/favicon.ico')

        plt.rcParams.update({'font.size': 7})
        figure = plt.figure(figsize=(15, 4), dpi=100)
        figure.patch.set_alpha(0.0)

        plotAirTemp = figure.add_subplot(1, 5, 1)
        plotAirTemp.set_title('AirTemp')
        plotAirTemp.set_xlabel('hours ago')
        plotAirTemp.set_ylabel('℃')
        plotAirTemp.axhspan(ymin=cropData.jsonCropBase['air_temp_low'],
                            ymax=cropData.jsonCropBase['air_temp_high'], facecolor='green', alpha=0.3)
        plotAirTemp.scatter(cropData.graphTimestamp,
                            cropData.graphAirTemp, color='green')
        plotAirTemp.plot(cropData.graphTimestamp, cropData.graphAirTemp)

        plotAirCo2 = figure.add_subplot(1, 5, 2)
        plotAirCo2.set_title('CO2')
        plotAirCo2.set_xlabel('hours ago')
        plotAirCo2.set_ylabel('ppm')
        plotAirCo2.axhspan(ymin=cropData.jsonCropBase['air_co2_low'],
                           ymax=cropData.jsonCropBase['air_co2_high'], facecolor='green', alpha=0.3)
        plotAirCo2.scatter(cropData.graphTimestamp,
                           cropData.graphAirCo2, color='green')
        plotAirCo2.plot(cropData.graphTimestamp, cropData.graphAirCo2)

        plotAirMoisture = figure.add_subplot(1, 5, 3)
        plotAirMoisture.set_title('Moisture')
        plotAirMoisture.set_xlabel('hours ago')
        plotAirMoisture.set_ylabel('%')
        plotAirMoisture.axhspan(ymin=cropData.jsonCropBase['air_moisture_low'],
                                ymax=cropData.jsonCropBase['air_moisture_high'], facecolor='green', alpha=0.3)
        plotAirMoisture.scatter(cropData.graphTimestamp,
                                cropData.graphAirMoisture, color='green')
        plotAirMoisture.plot(cropData.graphTimestamp,
                             cropData.graphAirMoisture)

        plotWaterTemp = figure.add_subplot(1, 5, 4)
        plotWaterTemp.set_title('WaterTemp')
        plotWaterTemp.set_xlabel('hours ago')
        plotWaterTemp.set_ylabel('℃')
        plotWaterTemp.axhspan(ymin=cropData.jsonCropBase['water_temp_low'],
                              ymax=cropData.jsonCropBase['water_temp_high'], facecolor='green', alpha=0.3)
        plotWaterTemp.scatter(cropData.graphTimestamp,
                              cropData.graphWaterTemp, color='green')
        plotWaterTemp.plot(cropData.graphTimestamp, cropData.graphWaterTemp)

        plotWaterTds = figure.add_subplot(1, 5, 5)
        plotWaterTds.set_title('TDS')
        plotWaterTds.set_xlabel('hours ago')
        plotWaterTds.set_ylabel('mg/L')
        plotWaterTds.axhspan(ymin=cropData.jsonCropBase['water_tds_low'],
                             ymax=cropData.jsonCropBase['water_tds_high'], facecolor='green', alpha=0.3)
        plotWaterTds.scatter(cropData.graphTimestamp,
                             cropData.graphWaterTds, color='green')
        plotWaterTds.plot(cropData.graphTimestamp, cropData.graphWaterTds)

        graph = FigureCanvasTkAgg(figure,  newWindow)

        graph.draw()
        graph.get_tk_widget().grid(column=0, row=0)

    def kakaoButton(self):
        kakao().login()
        # print(kakao.image_url)
        raw_data = urllib.request.urlopen(kakao.image_url).read()
        im = Image.open(io.BytesIO(raw_data))
        im = im.resize((100, 100))

        TK.kakaoImageData = ImageTk.PhotoImage(im)

        TK.kakaoImage = tkinter.Label(
            TK.kakaoFrame, image=TK.kakaoImageData, width=100, height=100)
        TK.kakaoImage.grid(column=0, row=1, padx=5, pady=5)

        TK.kakaoNickname = tkinter.Label(
            TK.kakaoFrame, text="이름 : " + kakao.nickname)
        TK.kakaoNickname.grid(column=0, row=2, padx=5, pady=5)
        cropData().getMember()
        TK.Auth = tkinter.Label(
            TK.kakaoFrame, text="권한 : " + cropData.jsonCropMember['auth'])
        TK.Auth.grid(column=0, row=3, padx=5, pady=5)

    def runWindow(self):
        TK.window.mainloop()

    def makeWindow(self):

        TK.window = tkinter.Tk()
        TK.window.wait_visibility(TK.window)
        TK.window.wm_attributes('-alpha', 1.0)
        TK.window.title("Hydroponics")
        TK.window.iconbitmap('res/favicon.ico')
        TK.window.geometry("200x270+0+0")
        TK.window.resizable(False, False)

        TK.buttonFrame = tkinter.Frame(TK.window)
        TK.buttonFrame.grid(column=0, row=0, padx=5, pady=5)

        TK.kakaoFrame = tkinter.Frame(TK.window)
        TK.kakaoFrame.grid(column=1, row=0, padx=5, pady=5)

        TK.summaryButtonImage = ImageTk.PhotoImage(file='res/info.png')
        TK.summaryButton = tkinter.Button(
            TK.buttonFrame, image=TK.summaryButtonImage)
        TK.summaryButton.bind("<Button>", TK.makeSummary)
        TK.summaryButton.grid(column=0, row=0, padx=5, pady=5)

        TK.graphButtonImage = ImageTk.PhotoImage(file='res/graph.png')
        TK.graphButton = tkinter.Button(
            TK.buttonFrame, image=TK.graphButtonImage)
        TK.graphButton.bind("<Button>", TK.makeGraph)
        TK.graphButton.grid(column=0, row=1, padx=5, pady=5)

        TK.photoButtonImage = ImageTk.PhotoImage(file='res/picture.png')
        TK.photoButton = tkinter.Button(
            TK.buttonFrame, image=TK.photoButtonImage)
        TK.photoButton.bind("<Button>", TK.makeGallery)
        TK.photoButton.grid(column=0, row=2, padx=5, pady=5)

        TK.settingButtonImage = ImageTk.PhotoImage(file='res/gear.png')
        TK.settingButton = tkinter.Button(
            TK.buttonFrame, image=TK.settingButtonImage)
        TK.settingButton.bind("<Button>", TK.makeSetting)
        TK.settingButton.grid(column=0, row=3, padx=5, pady=5)

        TK.loginImage = ImageTk.PhotoImage(file='res/kakao_login_medium.png')
        TK.kakaoLoginButton = tkinter.Button(
            TK.kakaoFrame, image=TK.loginImage)

        TK.kakaoLoginButton.bind("<Button>", TK.kakaoButton)

        TK.kakaoLoginButton.grid(column=0, row=0, padx=5, pady=5)

        # self.makeSummary()
        # self.makeGraph()


class cropData():

    def getCropBase(self):
        response = requests.get("http://redcomet.duckdns.org/getCropBase")
        cropData.jsonCropBase = response.json()
        print(cropData.jsonCropBase)

    def getCropLog(self):
        response = requests.get("http://redcomet.duckdns.org/getCropLog")
        cropData.jsonCropLog = response.json()

    def getCropLogs(self):
        response = requests.get("http://redcomet.duckdns.org/getCropLogs")
        cropData.jsonCropLogs = response.json()

        cropData.graphTimestamp = list()

        cropData.graphAirTemp = list()
        cropData.graphAirTempBool = list()

        cropData.graphAirCo2 = list()
        cropData.graphAirCo2Bool = list()

        cropData.graphAirMoisture = list()
        cropData.graphAirMoistureBool = list()

        cropData.graphWaterTemp = list()
        cropData.graphWaterTempBool = list()

        cropData.graphWaterTds = list()
        cropData.graphWaterTdsBool = list()

        now = int(time.time())

        # print(now)
        for data in cropData.jsonCropLogs:

            cropData.graphTimestamp.append((now - data['timestamp'])/60/60)

            cropData.graphAirTemp.append(data['air_temp'])
            if (data['air_temp'] < cropData.jsonCropBase['air_temp_low'] or data['air_temp'] > cropData.jsonCropBase['air_temp_high']):
                cropData.graphAirTempBool.append(False)
            else:
                cropData.graphAirTempBool.append(True)

            cropData.graphAirCo2.append(data['air_co2'])
            if (data['air_co2'] < cropData.jsonCropBase['air_co2_low'] or data['air_co2'] > cropData.jsonCropBase['air_co2_high']):
                cropData.graphAirCo2Bool.append(False)
            else:
                cropData.graphAirCo2Bool.append(True)

            cropData.graphAirMoisture.append(data['air_moisture'])
            if (data['air_moisture'] < cropData.jsonCropBase['air_moisture_low'] or data['air_moisture'] > cropData.jsonCropBase['air_moisture_high']):
                cropData.graphAirMoistureBool.append(False)
            else:
                cropData.graphAirMoistureBool.append(True)

            cropData.graphWaterTemp.append(data['water_temp'])
            if (data['water_temp'] < cropData.jsonCropBase['water_temp_low'] or data['water_temp'] > cropData.jsonCropBase['water_temp_high']):
                cropData.graphWaterTempBool.append(False)
            else:
                cropData.graphWaterTempBool.append(True)

            cropData.graphWaterTds.append(data['water_tds'])
            if (data['water_tds'] < cropData.jsonCropBase['water_tds_low'] or data['water_tds'] > cropData.jsonCropBase['water_tds_high']):
                cropData.graphWaterTdsBool.append(False)
            else:
                cropData.graphWaterTdsBool.append(True)

        print(cropData.graphTimestamp)

    def getCropSlot(self):
        response = requests.get("http://redcomet.duckdns.org/getCropSlot")
        cropData.jsonCropSlot = response.json()

    def getCropImage(self, slot):
        response = requests.get(
            f"http://redcomet.duckdns.org/getCropImage{slot}.png")
        cropData.jsonCropImage = response.json()

    def getMember(self):
        datas = {'token': kakao.token}
        response = requests.post(
            url="http://redcomet.duckdns.org/getMember",  json=datas)
        cropData.jsonCropMember = response.json()
        # print(cropData.jsonCropMember)

    def setCropBase(self, data):
        response = requests.post(
            url="http://redcomet.duckdns.org/setCropBase",  data=data)
        return response.json()


def main():
    kakao.token = ''
    crop = cropData()
    crop.getCropBase()
    crop.getCropLog()
    crop.getCropLogs()
    crop.getCropSlot()

    tk = TK()
    tk.makeWindow()
    tk.runWindow()

    # kakao = kakaoLogin()
    # kakao.login()
    # pass


if __name__ == "__main__":
    main()
