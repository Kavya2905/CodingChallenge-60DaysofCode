# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(input())
d = deque()
for i in range(N):
    n = input().split()
    if n[0]=='append':
        d.append(int(n[1]))
    elif n[0]=='appendleft':
         d.appendleft(int(n[1]))
    elif n[0]=='pop':
        d.pop()
    elif n[0]=='popleft':
         d.popleft()
    elif n[0]=='reverse':
         d.reverse()
    elif n[0]=='rotate':
         d.rotate(int(n[1]))
    elif n[0]=='remove':
         d.remove(n[1])
    elif n[0]=='remove':
         d.remove(n[1])
for i in d:
    print(i, end=' ')
