#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(num, steps):
    count = 0
    precount = count
    valley = 0
    hill = 0
    func = lambda step: step.replace("U","1") if step == "U" else step.replace("D","-1")
    step_list = [int(func(step)) for step in steps]
    for step in step_list:
        precount = count
        count = count + step
        if count < 0 and precount == 0:
            valley += 1
        elif count > 0 and precount == 0:
            hill += 1
    return hill

n = 8
#8
s = "UDDUUDDU"
#UDDDUDUU
print(countingValleys(n,s))
   
