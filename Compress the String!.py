# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s = input()
x = itertools.groupby(s)
for k,g in x:
    a = len(list(g)), int(k)
    print(a, end = ' ')
