#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[0:2] != '12' and s[-2:] == 'PM':
        hr = int(s[0:2]) + 12
        s = s.replace(s[0:2], str(hr))
        return s[: -2]
    elif s[-2:] == 'AM' and s[0:2] == '12':
        s = s.replace(s[0:2], '00')
        return s[: -2]
    else:
        return s[: -2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
