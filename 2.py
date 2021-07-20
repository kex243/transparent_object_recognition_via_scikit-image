import cv2
import numpy as np

from os import listdir
from os.path import isfile, join

mypath = "./input"
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]
counter = 0
for image in images:
    print (image)
    print (mypath +'/' +image)
    image_to_work = cv2.imread(mypath+'/'+image)

    # Convert to HSV
    hsv = cv2.cvtColor(image_to_work, cv2.COLOR_BGR2HSV)

    # Define lower and uppper limits of what we call "white-ish"
    sensitivity = 230
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)



    edges = cv2.Canny(image_to_work,0,250)
    image_inverted = abs(255-edges)






    inv1 = abs(255-mask)
    inv2 = abs(255-image_inverted)
    splitted = abs(inv1 +inv2)

    minus1 = abs(inv1-splitted)
    minus2 = abs(splitted-inv1)
    revminus1 = abs(255-splitted-inv1)
    revminus2 = abs(255-inv1-splitted)
    cv2.imwrite('./temp1/'+image[:-4]+ '.png', mask)
    #cv2.imwrite('inv2.png', inv2)
    #cv2.imwrite('inv1.png', inv1)
    cv2.imwrite('./temp2/'+image[:-4]+ '.png', image_inverted)
    #cv2.imwrite('splitted.png', splitted)
    #cv2.imwrite('minus1.png', minus1)
    #cv2.imwrite('minus2.png', minus2)
    #cv2.imwrite('revminus1.png', revminus1)
    #cv2.imwrite('revminus2.png', revminus2)
    counter += 1



cv2.destroyAllWindows()