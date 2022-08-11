# Day 1: Standard Deviation

import math
import os
import random
import re
import sys

def stdDev(arr):
    mean = sum(arr)/len(arr)
    diff_arr = []
    for i in arr:
        diff_arr.append((i-mean)**2)
    
    sd = math.sqrt(sum(diff_arr)/len(diff_arr))
    sd = round(sd, 1)
    print(sd)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)