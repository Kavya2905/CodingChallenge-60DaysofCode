#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    # Write your code here
    swaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                    
            else:
                swaps +=0
    
    print('Array is sorted in', str(swaps), 'swaps.')
    print("First Element:", a[0])
    print("Last Element:", a[-1])
        
