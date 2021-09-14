# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = input().split()
L = []
for i in range(int(X)):
    A = list(map(float, input().split()))
    L += [A]
    M = list(zip(*L))
    
for j in M:
    k = sum(list(j))
    print(k/int(X))
