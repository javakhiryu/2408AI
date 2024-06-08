import cv2
import  numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import os

#image = cv2.imread('live.png')
def scanimage(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(350,350))
    #plt.imshow(cv2.imread('myimage.png'))
    l = ['2.png','4.png','8.png','16.png','32.png','64.png','128.png','256.png','512.png','1024.png','2048.png']
    plt.show()

   
    def mydata(imgg):
        val = 0
        for i in l:
            img = deepcopy(imgg)
            checkimg = cv2.imread(f'data/{i}')
            checkimg= cv2.cvtColor(checkimg, cv2.COLOR_BGR2GRAY)
            w, h = checkimg.shape[::-1]

            res = cv2.matchTemplate(img,checkimg,cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where( res >= threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            if(len(loc[0]) > 0):
                val = int(i[:-4])
                #cv2.imshow('Image', img)
                #print("found: ",i)
                #cv2.waitKey()
        return val

    #def mydata(imgg):
    #    val = 0
    #    for i in l:
    #        img = deepcopy(imgg)
    #        checkimg_path = os.path.join('data', i)
#
    #        if not os.path.exists(checkimg_path):
    #            print(f"File {checkimg_path} does not exist. Skipping.")
    #            continue
#
    #        checkimg = cv2.imread(checkimg_path)
    #        if checkimg is None:
    #            print(f"Failed to read {checkimg_path}. Check file integrity.")
    #            continue
#
    #        checkimg = cv2.cvtColor(checkimg, cv2.COLOR_BGR2GRAY)
    #        w, h = checkimg.shape[::-1]
#
    #        img_height, img_width = img.shape
    #        if img_height < checkimg.shape[0] or img_width < checkimg.shape[1]:
    #            print(f"Template image {i} is larger than the source image. Skipping.")
    #            continue
#
    #        res = cv2.matchTemplate(img, checkimg, cv2.TM_CCOEFF_NORMED)
    #        threshold = 0.8
    #        loc = np.where(res >= threshold)
#
    #        for pt in zip(*loc[::-1]):
    #            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
#
    #        if len(loc[0]) > 0:
    #            val = int(i[:-4])
    #            # Uncomment these lines if you want to see the matched images
    #            #cv2.imshow('Image', img)
    #            #print("found: ", i)
    #            cv2.waitKey()
#
    #    return val
#



    array = []

    for i in range(0,350,88):
        row = []
        for j in range(0,350,90):
            img = image[i:80+i,j:80+j]
            #cv2.imshow("Split", img)
            #cv2.waitKey()
            row.append(mydata(img))
        array.append(row)
    return array



#myarray = scanimage(image)
#print(myarray)