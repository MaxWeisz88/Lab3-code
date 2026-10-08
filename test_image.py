import numpy as np
from skimage import io
import matplotlib.pyplot as plt

a = np.zeros((10,10))
a[:,:] = 0.0

a[2:4, 6:8] = 1.0
plt.imshow(a, cmap=plt.cm.gray, vmin=0.0, vmax=1.0)
plt.show()

#function to create a square of the color `shade` in an image given the start for the 
# upper left corner and width of the desired square
def makesquare(initial_image, row_ul, col_ul, width, shade):
    copy = initial_image.copy()
    copy[row_ul : row_ul + width, col_ul : col_ul + width] = shade
    #make a square in the image that has width and height equal to `width`
    return copy
