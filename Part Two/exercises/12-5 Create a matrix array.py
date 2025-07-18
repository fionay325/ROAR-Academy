import numpy as np
def set_array(L, rows, cols):
    temp = np.empty((rows,cols))
    for i in range(rows):
        for j in range(cols):
            temp[(i,j)] = L[rows * i + j]
    print(temp)
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
set_array(v, 3, 3)