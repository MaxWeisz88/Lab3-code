from skimage import data,io
from scipy import ndimage
import numpy as np
import skimage as ski

# Load in the test image 
a=io.imread("audrey_lnoise.png", as_gray=True)
a=ski.img_as_float64(a)
a*=1/(a[:].max())

# Initialize a copy of the image 
(y,x)=a.shape # type: ignore
b=np.copy(a)

# for j in range(1,y-1):
#     for i in range(1,x-1):

#         # Create list of nearby points
#         l=[a[j,i],a[j+1,i],a[j-1,i],a[j,i-1],a[j,i+1]]

#         # Set output pixel to be median
#         # of the list
#         b[j,i]=np.median(l)

#function to choose how to shape the window of pixels to get median from
def denoise_by_shape(source, width, height):
    result = np.copy(source) 

    # create a window with the width and height specified in parameters
    top = height // 2 
    bottom = height - top
    left = width // 2
    right = width - left

    for j in range(1,y-1):
        for i in range(1,x-1):
            # Create array of `width` and `height` around pixel (j,i)
            window = source[max(j - top, 0):min(j + bottom, y), 
                    max(i - left, 0):min(i + right, x)]
            # Set output pixel to be median of the array
            result[j,i]=np.median(window)

    return result

def save_by_shape(source, width, height):
    source_to_save = ski.util.img_as_ubyte(np.clip(source, 0, 1))
    io.imsave(f"{width}by{height}audrey_denoise.png", 
              source_to_save)

save_by_shape(denoise_by_shape(a, 1, 2), 1, 2)
save_by_shape(denoise_by_shape(a, 1, 3), 1, 3)
save_by_shape(denoise_by_shape(a, 3, 1), 3, 1)
save_by_shape(denoise_by_shape(a, 1, 4), 1, 4)
save_by_shape(denoise_by_shape(a, 1, 5), 1, 5)
save_by_shape(denoise_by_shape(a, 10, 1), 10, 1)
b = denoise_by_shape(a, 1, 3)
b_to_save = ski.util.img_as_ubyte(np.clip(b, 0, 1))
# Plot the image
io.imsave("audrey_denoise.png",b_to_save)
