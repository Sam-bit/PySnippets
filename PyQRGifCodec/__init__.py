import base64

import qrcode

from PyQRGifCodec.encode import Encoder


def QrEncode(bytes_read, size, recLevel):
    qr = qrcode.QRCode(
        version=1,
        error_correction=recLevel,
        box_size=size,
        border=4,
    )
    qr.add_data(bytes_read)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")


def AnimatedGif(bytes_read: bytes, imgSize: int, FPS: int
                , size: int, recLevel: int):
    b64string = base64.b64encode(bytes_read)
    print(b64string)
    chunks = Encoder(size)


fileName: str = "Screenshot_2022-10-21-06-47-38-83_92b64b2a7aa6eb3771ed6e18d0029815.jpg"
splitSize:int = 100  # Chunk size for data split per frame
size:int = 300  # QR code size
FPS:int = 5  # Animation FPS
recLevel:int = qrcode.constants.ERROR_CORRECT_M
output = ''
if output == '':
    output = fileName + ".gif"
with open(fileName, "rb") as f:
    bytes_read:bytes= f.read()
print(bytes_read)
out = AnimatedGif(bytes_read, size, FPS, splitSize, recLevel)
