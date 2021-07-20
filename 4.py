import cv2
import numpy as np

from os import listdir
from os.path import isfile, join

mypath = "./temp3"
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for image in images:
    print (image)
    image1 = cv2.imread("./temp1/"+str(image))
    print (image1)
    image2 = cv2.imread("./temp3/"+str(image))


    inv1 = abs(255-image1)
    inv2 = abs(255-image2)
    splitted = abs(inv1 +inv2)
    splitted = abs(255-splitted)

    cv2.imwrite('maskfinal.png', splitted)


    kernel = np.ones((2,2), np.uint8)
    img_erosion = cv2.erode(splitted, kernel, iterations=10)




    cv2.imwrite("./output/"+str(image)[:-4]+'.png', img_erosion)

