#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    a = sorted(arr)
    arr1 = []
    arr2 = []
    for i in range(0, len(arr)-1):
        arr1.append(a[i])
    for j in range(1, len(arr)):
        arr2.append(a[j])
    
    print(sum(arr1), sum(arr2))    
   

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
