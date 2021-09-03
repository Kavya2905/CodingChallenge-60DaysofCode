# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    m = int(input())
    A = set(input().split())
    n = int(input())
    B = set(input().split())
    if m <= n:
       if A.intersection(B) == A:
        print("True")
       else:
        print("False")
    else:
        print('False')
