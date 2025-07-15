from matplotlib import image
from matplotlib import pyplot
import os


filename = "/Users/fiona/Documents/GitHub/ROAR-Academy/Part Two/samples/lenna.bmp"
data = image.imread(filename)
pyplot.imshow(data)