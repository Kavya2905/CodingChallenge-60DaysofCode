# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
M = map(int, input().split())
n = int(input())
N = map(int, input().split())
eng_or_french = set(M).union(set(N))
print(len(eng_or_french))
