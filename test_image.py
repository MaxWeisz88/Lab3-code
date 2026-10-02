import numpy as np
from skimage import io
import matplotlib.pyplot as plt

a = np.zeros((10,10))
a[:,:] = 0.0

a[2:4, 6:8] = 1.0
plt.imshow(a, cmap=plt.cm.gray, vmin=0.0, vmax=1.0)
plt.show()

