# Day 1: Quartiles

import math
import os
import random
import re
import sys
from statistics import median

def quartiles(arr):
    arr = sorted(arr)
    if len(arr)%2 != 0:
        q2_index = int((len(arr)-1)/2)
        q2 = arr[q2_index]
        
        q1_range = arr[:int((len(arr)-1)/2)]
        q3_range = arr[q2_index+1:]
        
        if len(q1_range)%2 != 0:
            q1_index = int((len(q1_range)-1)/2)
            q1 = q1_range[q1_index]
            
            q3_index = int((len(q3_range)-1)/2)
            q3 = q3_range[q3_index]
        
        elif len(q1_range)%2 == 0:
            q1_index_1 = int((len(q1_range)-1)/2)
            q1_index_2 = int((len(q1_range)+1)/2)
            q1 = (q1_range[q1_index_1]+q1_range[q1_index_2])/2
            
            q3_index_1 = int((len(q3_range)-1)/2)
            q3_index_2 = int((len(q3_range)+1)/2)
            q3 = (q3_range[q3_index_1]+q3_range[q3_index_2])/2
    
    elif len(arr)%2 == 0:
        q2_index_1 = int((len(arr)/2)-1)
        q2_index_2 = int(len(arr)/2)
        q2 = (arr[q2_index_1]+arr[q2_index_2])/2
        
        q1_range = arr[:int(len(arr)/2)]
        q3_range = arr[int(len(arr)/2):]
        
        if len(q1_range)%2 != 0:
            q1_index = int((len(q1_range)-1)/2)
            q1 = q1_range[q1_index]
            q3_index = int((len(q1_range)-1)/2)
            q3 = q3_range[q3_index]
        
        elif len(q1_range)%2 == 0:
            q1_index_1 = int((len(q1_range)/2)-1)
            q1_index_2 = int(len(q1_range)/2)
            q3_index_1 = int((len(q3_range)/2)-1)
            q3_index_2 = int(len(q3_range)/2)
            q1 = (q1_range[q1_index_1]+q1_range[q1_index_2])/2
            q3 = (q3_range[q3_index_1]+q3_range[q3_index_2])/2
    print(int(q1))
    print(int(q2))
    print(int(q3))     
         

if __name__ == '__main__':
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)