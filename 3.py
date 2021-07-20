import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import os
from skimage import io

from os import listdir
from os.path import isfile, join

mypath = "./temp2"
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for image in images:
    cwd = os.path.abspath(os.getcwd())

    filename = os.path.join(cwd + './temp2', image)

    img = io.imread(filename)

    img = rgb2gray(img)
    #    alpha1, beta1, gamma1, maxpx1 = 0.065, 0.1, 0.005, 1
    alpha1, beta1, gamma1, maxpx1 = 0.065, 0.1, 0.005, 1

    s = np.linspace(0, 2*np.pi, 700) #700
    r = 690 + 450*np.sin(s) #450
    c = 520 + 250*np.cos(s) #200
    init = np.array([r, c]).T


    snake = active_contour(gaussian(img, 3, preserve_range=False),
                           init, alpha=alpha1, beta=beta1, gamma=gamma1,max_px_move = maxpx1)
    my_dpi=97
    fig, ax = plt.subplots(figsize=(1024/my_dpi, 1280/my_dpi), dpi=my_dpi)


    ax.imshow(img, cmap=plt.cm.gray)

    ax.plot(snake[:, 1], snake[:, 0], color="black", lw=6)
    ax.fill(snake[:, 1], snake[:, 0], color="black", lw=6)

    ax.set_axis_off()
    plt.axis('off')

    plt.savefig('./temp3/'+ image[:-4] + '.png', bbox_inches='tight', pad_inches = 0, dpi=126)
