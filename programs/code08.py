import numpy as np

def make_array():
    arr = np.zeros((3, 3), dtype=float)
    for i in range(0, 3):
        for j in range(0, 3):
            arr[i,j] =  2 * np.random.randint(1, 5)
    return arr

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

arr = make_array()

m, n = np.shape(arr)
my = 0
i = 1
print(arr)
while (my < m):
    arr[my] = 1 / arr[my, my] * arr[my]
    print(arr)
    while (my + i < m):
        arr[my + i] = arr[my + i] + -1 * arr[my+i, my] * arr[my]
        print(arr)
        i += 1
    i = 1
    my += 1
print(arr)