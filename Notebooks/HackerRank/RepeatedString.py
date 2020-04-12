#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = s.count("a")
    req_len = n / len(s)
    primary_count = count * int(req_len)
    secondary_count = 0
    print(f'primary count:{primary_count}')
    print(f'faction: {req_len%1}')
    if req_len % 1 != 0:
        remaining_chars = math.ceil(round(len(s) * (req_len % 1), 2))
        print(f'remaining characters: {remaining_chars}')
        secondary_count = s.count("a",0,remaining_chars)
        print(f'secondary count: {secondary_count}')
    total_count = primary_count + secondary_count
    return total_count

#s = "aba"
#n = 10
s = "bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc"
n = 649606239668
#162401559918
#s = "a"
#n = 1000000000000
result = repeatedString(s, n)
print(f'result: {result}')