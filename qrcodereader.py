# Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read

# Create QR Code

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
link = "https://web.facebook.com/Luunnnaaa/"
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="pink")
img.save("qrcodechan.png")


# QR Code Scanner
import cv2
import webbrowser
import datetime
vcapture = cv2.VideoCapture(0)
vdetector = cv2.QRCodeDetector()
while True:
    _, img = vcapture.read()
    data, one, _ = vdetector.detectAndDecode(img)
    if data:
        read = data
        break
    cv2.imshow('QRCode Scanner', img)
    if cv2.waitKey(1)==ord('a'):
        break
redirect = webbrowser.open((str(read)))
vcapture.release(read)
cv2.destroyAllWindows