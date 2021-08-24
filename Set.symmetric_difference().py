# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
m = input().split()
N = int(input())
n = input().split()
print(len(set(m)^set(n)))
