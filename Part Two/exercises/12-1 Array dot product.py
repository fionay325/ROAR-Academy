import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot
import numpy as np

def project_on_3D(v):
    e0 = np.array([1., 0., 0.])
    e1 = np.array([0., 1., 0.])
    e2 = np.array([0., 0., 1.])
    return v@e0, v@e1, v@e2

v = np.array([2.,2.,4.])
print(project_on_3D(v))

    