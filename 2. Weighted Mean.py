# Day 0: Weighted Mean

import math
import os
import random
import re
import sys

def weightedMean(X, W):
    weight = sum(W)
    lst = []
    for i in range(len(X)):
        for j in range(len(W)):
            if i==j:
                lst.append(X[i]*W[j])
    result = float(sum(lst)/weight)
    main_result = round(result, 1)
    print(main_result)
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)