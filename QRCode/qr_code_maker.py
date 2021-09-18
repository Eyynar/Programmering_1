import qrcode
from PIL import Image


content = input("Enter text:")

image = qrcode.make(content)
image.save("QR.jpg")
show_image = Image.open("QR.jpg")
show_image.show()



