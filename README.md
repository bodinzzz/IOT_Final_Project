# 智慧分藥機

這是一個利用LineBot及樹莓派的智慧分藥機，旨在協助減少醫療疏失以及護理師與藥師的負擔，同時簡化分藥流程。此系統可將藥囑數據化成QRcode，病人可透過攝影鏡頭進行解碼，取得電子藥囑，並利用智慧分藥機自行取藥。


#### 軟體與硬體

此系統主要使用以下軟體與硬體：

- Flask：一個使用Python編寫的輕量級Web應用框架，用於建立Web伺服器以及與Line Bot進行互動。
- Line Bot：一個Line提供的聊天機器人平台，用於與使用者進行互動。
- Raspberry Pi 4：一種迷你電腦，可用於控制整個智慧分藥機。
- 攝影鏡頭模組：一種攝影鏡頭，可用於掃描QRcode。
- Servo Motor：一種電機，用於控制藥盒開啟與關閉。
- DHT22 Temperature Humidity Sensor Module：一種溫濕度傳感器，用於監測環境溫度與濕度。

#### 線路圖與裝置
![](https://i.imgur.com/lGm3PFZ.png)
![](https://i.imgur.com/qneD1jx.jpg)


#### Step1 在樹梅派架設LineBot
##### 1. 去官網申請Line bot 帳號
- 官網連結 : https://developers.line.biz/zh-hant/
- Create channel and Message API
- 取得Channel access token、Channel secret
##### 2. 在樹梅派上安裝所需套件
>pip3 install Flask

>pip3 install line-bot-sdk

- 運行官方範例，可看到如下畫面
![](https://i.imgur.com/8o75Kiq.png)

#### Step2 建立外網連結
##### 1. 在樹梅派上安裝所需套件並解壓縮

>sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip

>sudo unzip ngrok-stable-linux-arm.zip

##### 2. 在ngrok官網取得Authtoken
- 官網連結 : https://ngrok.com/
- ![](https://i.imgur.com/zRksulZ.png)

##### 3. 獲得Webhook URL
- 在樹梅派輸入：
>./ngrok authtoken "你的Authtoken"

>./ngrok http 5000

![](https://i.imgur.com/iUKZQB1.jpg)
- 將fowarding 的https網址填入webhook URL，並加上"/callback"，點擊verify，若success即成功

![](https://i.imgur.com/sVwekl1.jpg)

注意:
- 每一次執行./ngrok http 5000都會產生不同的網址，需要重新verify webhook URL
- 若verify失敗，請檢查是否已經執行機器人的主程式(app.py)

#### Step2 撰寫程式碼

- app.py : 主程式碼
- medicine_dispenser.py : 負責控制硬體
- qrcode_maker.py : 建立qrcode程式碼並上傳imgur取回https網址
  - 所需套件:
  > pip3 install qrcode

  > pip3 install imgurpython

  > pip3 install requests

  > pip3 install pyimgur
  - 註冊帳號並取得client_id(側欄的register an application)
  官網連結：https://imgur.com/
  ![](https://i.imgur.com/4WgFndE.png)

- camera.py : 負責解碼Qrcode
  所需套件:
  > pip3 install libzbar0
  > pip3 install pyzbar
  > pip3 install opencv-python

- sensor.py : 負責控制溫濕度感測器
  所需套件:
  >pip3 install adafruit-circuitpython-dht

  >sudo apt-get install libgpiod2

#### DEMO影片連結:
https://youtu.be/Xn7w7JaX70g


Reference
imgur:
https://pyimgur.readthedocs.io/en/latest/
https://ithelp.ithome.com.tw/articles/10241006
pyzbar:
https://tw511.com/a/01/22634.html
DHT22:
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
