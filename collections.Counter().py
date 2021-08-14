# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
N = Counter(map(int, input().split()))
T = int(input())



earning = 0
for i in range(T):
    size, cost = map(int, input().split())
    if N[size]:
        N[size] -= 1
        earning += cost
print(earning)
        
