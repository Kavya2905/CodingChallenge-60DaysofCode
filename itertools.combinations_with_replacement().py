# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, n = input().split()
a = (list(combinations_with_replacement(sorted(s),int(n))))
for i in a:
    print(''.join(i))
