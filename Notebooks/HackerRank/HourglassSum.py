import math
import os
import random
import re
import sys
import numpy as np

# Row summation function:
def rowSums(arr):
    row_sum = []
    for row in arr:
        row_sum.append(sum(row))
    return row_sum

# Column summation function:
def colSums(arr):
    col_sum = []
    for col in range(len(arr)):
        col_sum.append(arr[0][col]+arr[1][col]+arr[2][col]+arr[3][col]+arr[4][col]+arr[5][col])
    return col_sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(rowSums(arr))
    print(colSums(arr))
    return True


arr = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]
]
arrRand = np.random.randint(0, 6, size=6)
print(arr)
print(arrRand)
result = hourglassSum(arr)
print(result)
print(sys.version)

