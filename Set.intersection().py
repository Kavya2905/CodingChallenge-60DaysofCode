# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
m = set(map(int, input().split()))
N = int(input())
n = set(map(int, input().split()))
common = m.intersection(n)
print(len(common))
