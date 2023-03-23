from __future__ import unicode_literals
from typing import Text
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from medicine_dispenser import angle_to_duty_cycle, test
from qrcode_maker import make
from camera import take_picture
from sensor import take_sensor_data

app = Flask(__name__)

# LINE 聊天機器人的基本資料你
line_bot_api = LineBotApi('SECRET_ID')
handler = WebhookHandler('SECRET_ID')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 接收訊息的路由
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    message = event.message.text
    if message == 'dispense':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='how many?'))
    elif message.isdigit():
        image_message = ImageSendMessage(
            original_content_url = make(message),
            preview_image_url = make(message)
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        #line_bot_api.push_message
    elif message == 'check status':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=take_sensor_data()))
    elif message == 'get medicine':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='ok'))
        take_picture()
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='what?'))
    

if __name__ == "__main__":
    app.run()