# ENSF338W23 Assignment 2
Source code files for ENSF 338 Winter 2023, Assignment 2.

### Installations:
Files ex1.5.py and ex2.2.py use MatPlotLib in order to plot the timing results. In order for this to happen, pip install MatPlotLib into your directory or into a virtual environment. After this, the programs should be able to run as expected.


### Files:
**ex1.3.py**: In the assignment handout was a given Fibonacci Sequence with the use of recursion. The question states: "Implement a version of the code above that use memoization to improve performance. Provide this as ex1.3.py", which is provided in this repository as such. The Python files continues from the given code segement, but instead uses the method of memoization to improve the overall performance of the code. 
Below is the given code segment from the assignment hand-out:
```python
def func(n):
  if n == 0 or n == 1:
    return n
  else:
    return func(n-1) + func(n-2)
```

**ex1.5.py**: The question states: "Time the original code and your improved version, for all integers between 0 and 35, and plot the results. Provide the code you used for this as ex1.5.py", in the said file, I've added additional code to compare the given Fibonacci function as well as the memoized version of it. This file uses MatPlotLib to compare the timing results of the functions through line-graphs, and display it to the user. 

**ex2.2.py**: The question states: "Test the code on all the inputs at: https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json. Plot timing results. Provide your timing/plotting code as ex2.2.py". Taking the JSON file, MatPlotLib was used to calculate the amount of time that was used for using the given QuickSort algorithm in the assignment. Here, the input values are the corresponding amount of inputs in the JSON file, and the timing is displayed on the Y-Axis. Finally, a line-graph is outputted towards the user to display the timing comparisons.
Below is the given code sgement for the QuickSort algorithm from the assignment hand-out:
```python
import sys
sys.setrecursionlimit(20000)

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
```

**ex2.5.json**: This is a JSON file that is altered from https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json. Here, the `random` module is imported so the inputs inside of the JSON file can be rearranged in order for the given code to enhance the performance of the given QuickSort algorithm. 
Below is a segment of the code I used to randomize the inputs inside of the JSON file:
```python
import json
import random

with open("ex2.json", "r") as file:
    inputVals = json.load(file)

for arr in inputVals:
    random.shuffle(arr)

with open("ex2.5.json", "w") as file:
    json.dump(inputVals, file)
```


### Credits:
The given code segments (except the last one to randomize inputs of a JSON file) was given in a handout. This is from ENSF 338, Winter 2023 and all credits are given towards Professor Lorenzo de Carli and Professor Maan Khedr.
