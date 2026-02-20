import random
import time

def linearSearch(arr, sn):
    s = 0
    for i in range(len(arr)):
        s += 1
        if arr[i] == sn:
            return i, s
    return -1, s

def binarySearch(arr, sn):
    s = 0
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        s += 1
        if arr[mid] == sn:
            return mid, s
        if arr[mid] < sn:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, s

def bubbleSort(arr):
    s = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i - 1):
            s += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, s

sumL = 0
sumB = 0
rep = int(input("Repeat test how many times: "))
for i in range(rep):
    arr = [random.randint(1, 50) for n in range(50)]
    print(arr)
    sortedArr, _ = bubbleSort(arr)
    sn = random.randint(1, 50)
    _ , lChecks = linearSearch(sortedArr, sn)
    sumL += lChecks
    _ , bChecks = binarySearch(sortedArr, sn)
    sumB += bChecks
    print(f"Search number: {sn} | Linear: {lChecks} elements checked | Binary: {bChecks} elements checked\n")
    time.sleep(0.5)
lAvg = sumL / rep
bAvg = sumB / rep
print(f"Linear: {round(lAvg, 3)} average elements checked | Binary: {round(bAvg, 3)} average elements checked")