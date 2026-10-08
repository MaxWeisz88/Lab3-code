import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from test_image import makesquare

# function to create equally spaced squares inside of each other of alternating shade 
# given the desired number of squares and the total width/height of the square plot
def make_surrounding_squares(num_squares, total_size):
    # amount to increase each square by so the squares are proportionate
    step = total_size // (2 * num_squares) 
    
    # make initial black square the size of total_size x total_size
    square = makesquare(np.zeros((total_size, total_size)), 0, 0, total_size , 0)
    for i in range(1, num_squares):
        x = i * step # set amount to push square in from edges
        # find the side length by subtracting the amount it is
        # pushed in the center by on both sides
        side = total_size - (2 * x)
        # alternate shade between even and odd i, so every other repetition
        if i % 2 == 0:
            shade = 0
        else:
            shade = 1
        # make the smaller square nested inside the larger squares
        square = makesquare(square, x, x, side, shade)
    plt.imshow(square, cmap=plt.cm.gray, vmin=0.0, vmax=1.0)
    plt.show()

make_surrounding_squares(5,200) # function call to create left image
make_surrounding_squares(10,200) # function call to create right image
# make_surrounding_squares(100,200)
