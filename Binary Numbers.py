#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = bin(n)
    b = a[2:]
    count = 0
    result = 0
    for i in b:
        if i == '1':
            result += 1
        else:
            count = max(count, result)
            result = 0
    print(max(count, result))
            
