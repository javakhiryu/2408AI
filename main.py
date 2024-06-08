from ppadb.client import Client
import time
import os
import cv2 as cv
import manager
import divimage
import numpy as np

os.system('adb start-server')


adb = Client(host='localhost', port=5037)


devices = adb.devices()
device = devices[0]

if len(devices) == 0:
    print( "No devices found")
    
print("Connected devices:",devices)
print(devices)


totalmoves = 0
moves = 0
runs = int(input("Enter initial runs number(prefered in range 100 to 1000) : "))

try:

    while True:
        image = device.screencap()
        img = cv.imdecode(np.frombuffer(image, np.uint8), cv.IMREAD_COLOR)
        # with open(f'live.png','wb') as f:
        #     f.write(image)
        # image = cv.imread(f"live.png")
        image = cv.resize(img,(400,900))
        #cv.imshow("Starter",image)
        #cv.waitKey()
        #image = image[328:690,28:370]     # change this accordinf to your screenresolution 
                                          # (This values are only for screen with resolution of 2340 * 1080 resolution)
        image = image[279:648,10:380] 

        #cv.imshow("Croped",image)
        #cv.waitKey()


        #cv.imwrite("live.png",image)
        #cv.imshow("image",image)
        #cv.waitKey()
        #break
        

        array = divimage.scanimage(image)
        move = manager.runa(array,runs)
        print(array)
        print(move)

        if move['move'] == 'u':
            device.shell(f'input swipe 500 1000 500 600 25')
        if move['move'] == 'd':
            device.shell(f'input swipe 500 600 500 1000 25')
        if move['move'] == 'r':
            device.shell(f'input swipe 200 1000 700 1000 25')  
        if move['move'] == 'l':
            device.shell(f'input swipe 700 1000 200 1000 25') 

        if moves == 30:
            runs+=10
            moves = 0
except Exception as e:
    print(e)
print("Total moves",totalmoves)
print("Final runs",runs)
