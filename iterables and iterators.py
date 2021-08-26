# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
alpha = input().split()
m = int(input())
num = [i for i in range(1,n+1)]
l = list(combinations(alpha, m))
a_list = [e for e in l if 'a' in e]
print(len(a_list)/len(l))

    
