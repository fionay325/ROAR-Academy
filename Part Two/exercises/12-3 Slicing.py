import numpy as np
u = np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])
print(u[0:6,1])
print(u[1,2:4])
print(u[2:4,4:6])
print(u[2:5:2,0:6:2])