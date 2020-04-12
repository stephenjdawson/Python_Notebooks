#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    path = 0
    step = 0
    for i in range(len(c)):
        if i <= len(c)-3 and c[i+2] != 1 and i == step:
            path += 1
            step = i+2
        elif i < len(c)-1 and c[i+1] != 1 and i == step:
            path += 1
            step = i+1
    return path


c = [0,1,0,0,1,0,0]
print(jumpingOnClouds(c))