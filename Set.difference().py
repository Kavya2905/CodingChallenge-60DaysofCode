# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
A = map(int, input().split())
N = int(input())
B = map(int, input().split())
print(len(set(A).difference(set(B))))
