# Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read

# Create QR Code

import qrcode
qrcd = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    boxsize=11,
    border=5,
)
link = "https://web.facebook.com/Luunnnaaa/"
qrcd.add_data(link)
qrcd.make(fit=True)
img = qrcd.make_image(fill_color="pink", back_color="black")
img.save("qrcodechan.png")