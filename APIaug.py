
import base64
import os

def GeraQRcode(x,tipo):
    img_string = x.text[22:]
    imgdata = base64.b64decode(img_string)
    if not os.path.isdir("QRcodes"):
        os.mkdir('QRcodes')
    filename = f'QRcodes\qrcode_{tipo}.jpg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)
