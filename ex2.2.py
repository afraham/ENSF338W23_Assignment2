import sys
import json
import time
import matplotlib.pyplot as plt
import threading

sys.setrecursionlimit(20000)
threading.stack_size(33554432)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

###


with open("ex2.json", "r") as file:
    inputVals = json.load(file)

times = []
for arr in inputVals:
    startTime = time.time()
    func1(arr, 0, len(arr) - 1)
    endTime = time.time()
    times.append(endTime - startTime)

plt.plot(times)
plt.xlabel("Input Value")
plt.ylabel("Time (seconds)")
plt.show()
