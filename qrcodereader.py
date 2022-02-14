# Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read


import cv2 
import numpy as np
import datetime
from pyzbar.pyzbar import decode 

CamCapture = cv2.VideoCapture(0)
CamCapture.set(3,1080) #width
CamCapture.set(4,720) #height

CamScanner = True
while CamScanner == True:
    success, frame = CamCapture.read()

    for captureinfomartions in decode(frame):
        #Convert infos to text file
        txt_file = open("Data.txt", "w")
        txt_file.write(f"{captureinfomartions.data.decode('utf-8')}\n" )
        
        #Add the time and date when data is scanned
        Date = datetime.datetime.now()
        txt_file.write(Date.strftime("Date: %m/%d/%y \n"))
        txt_file.write(Date.strftime("Time: %H:%M:%S"))  
        txt_file.close()

        #Add effects for the program
        Filename = "SCANNING COMPLETED!"
        Qr_code_detector = np.array([captureinfomartions.polygon],np.int32)
        Qr_code_detector = Qr_code_detector.reshape((-1,1,2))
        cv2.polylines(frame, [Qr_code_detector], True, (0,128,0), 5)
        Qr_code_detector_2 = captureinfomartions.rect
        cv2.putText(frame, Filename, (Qr_code_detector_2 [0], Qr_code_detector_2[1]), cv2.FONT_HERSHEY_DUPLEX, 0.9,(0,128,0), 2)
               
    cv2.imshow('Aleja QR Code Scanner', frame)
    cv2.waitKey(1)