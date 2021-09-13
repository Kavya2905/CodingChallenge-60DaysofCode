# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    operation, length = input().split()
    B = set(map(int, input().split()))
    if operation == "intersection_update": 
        A.intersection_update(B)
    
    elif operation == "update": 
        A.update(B)
    
    elif operation == "symmetric_difference_update": 
        A.symmetric_difference_update(B)
    
    else:
        A.difference_update(B)
        
print(sum(A))
