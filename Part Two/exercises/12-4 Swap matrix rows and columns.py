import numpy as np
def swap_rows(M, a, b):
    if len(M.shape)<2:
        raise ValueError("Matrix must have at least two dimensions")
    temp = M[a].copy()
    M[a] = M[b].copy()
    M[b] = temp
def swap_cols(M, a, b):
    if len(M.shape)<2:
        raise ValueError("Matrix must have at least two dimensions")
    for i in range(M.shape[0]):
        temp = M[i, a].copy()
        M[i, a] = M[i, b].copy()
        M[i, b] = temp
v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
swap_rows(v, 0, 1)
print(v)
swap_cols(v, 0, 1)
print(v)