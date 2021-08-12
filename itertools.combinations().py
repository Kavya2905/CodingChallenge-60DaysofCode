# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s, n = input().split()
m = sorted(list(s))
k = ''.join(m)
for i in range(1, int(n)+1):
    x = list(combinations(str(k),i))
    for j in x:
        y = ''.join(list(j))
        print(y)   
