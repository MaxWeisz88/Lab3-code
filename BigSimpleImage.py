import numpy as np
import matplotlib.pyplot as plt
from skimage import io

#function to create a square of the color `shade` in an image given the start for the 
# upper left corner and width of the desired square
def makesquare(initial_image, row_ul, col_ul, width, shade):
    copy = initial_image.copy()
    copy[row_ul : row_ul + width, col_ul : col_ul + width] = shade
    #make a square in the image that has width and height equal to `width`
    return copy

#function to create equally spaced/sized squares inside of each other of alternating shade 
# given the desired number of squares and the total width/height of the square plot
def make_surrounding_squares(num_squares, total_size):
    step = total_size // (2 * num_squares) 
    square = makesquare(np.zeros((total_size, total_size)), 0, 0, total_size , 0)
    for i in range(1, num_squares):
        x = i * step 
        side = total_size - (2 * x)
        if i % 2 == 0:
            shade = 0
        else:
            shade = 1
        square = makesquare(square, x, x, side, shade)
    plt.imshow(square, cmap=plt.cm.gray, vmin=0.0, vmax=1.0)
    plt.show()

make_surrounding_squares(5,200)
make_surrounding_squares(10,200)
make_surrounding_squares(100,200)
