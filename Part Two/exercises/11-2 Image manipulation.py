from matplotlib import image
from matplotlib import pyplot
from PIL import Image
from scipy.ndimage import zoom
import numpy as np
import os


filename = "/Users/fiona/Documents/GitHub/ROAR-Academy/Part Two/samples/lenna.bmp"
data = Image.open(filename)
data = np.array(data)
x, y = data.shape[:2]


flagdata = Image.open("/Users/fiona/Documents/GitHub/ROAR-Academy/Part Two/exercises/unitedstatesflag.png") 
flagdata = np.array(flagdata)
row, col = flagdata.shape[:2]

if x < row and y < col:
    new_data = zoom(data, (2, 2, 1))
new_x, new_y = new_data.shape[:2]

for w_width in range(row):
    for w_range in range(y - col, y+1):
        new_data[w_width, w_range] = flagdata[w_width, w_range]
pyplot.imshow(new_data)
pyplot.show()

