import numpy as np

def g_interchange(arr):
    return arr

def g_multiply(arr):
    arr[0] = 1 / arr[0, 0] * arr[0]
    return arr

def g_add(arr):
    arr[1] = arr[1] + (-1 * arr[1, 0]) * arr[0]
    return arr

def ga_solve(arr):
    for i in range(0, m):
        if arr[i, i] != 0:
            g_multiply(arr)
            g_add(arr)
    return arr

arr = [[3, 4, 5], [6, 7, 8]]
arr = np.array(arr, float)
m, n = np.shape(arr)
print(ga_solve(arr))
print(m, n)