# Day 1: Interquartile Range

import math
import os
import random
import re
import sys
import statistics as st

def interQuartile(n, values, freqs):
    s = []
    for i in range(n):
        s += [values[i]] * freqs[i]
    N = sum(freqs)
    s.sort()

    if n%2 != 0:
        q1 = st.median(s[:N//2])
        q3 = st.median(s[N//2+1:])
    else:
        q1 = st.median(s[:N//2])
        q3 = st.median(s[N//2:])

    iqr = round(float(q3-q1), 1)
    print(iqr)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(n, val, freq)