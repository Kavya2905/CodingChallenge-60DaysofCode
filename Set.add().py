# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = set()
for i in range(n):
    x = input()
    m.add(x)
print(len(m))
