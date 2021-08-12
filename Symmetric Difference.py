# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a =  map(int, input().split())
N = int(input())
b = map(int, input().split())
A = set(a)
B = set(b)
K = []
X = list(A.difference(B))
for i in X:
    K.append(i)
Y = list(B.difference(A))
for j in Y:
    K.append(j)
for m in sorted(K):
    print(m)
