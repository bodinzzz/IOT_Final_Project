import qrcode # 匯入模組
from imgurpython import ImgurClient
import pyimgur

client_id = 'MY_CLIENT_ID'

def make(num):
    img = qrcode.make(num) # QRCode資訊
    PATH = "prescription.png"
    img.save(PATH) # 儲存圖片
    im = pyimgur.Imgur(client_id)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link