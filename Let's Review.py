# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for k in range(n):
    t = str(input())
    a = [t[i] for i in range(0, len(t), 2)]
    a = ''.join(a)
    b = [t[j] for j in range(1, len(t), 2)]
    b = ''.join(b)
    print(a + ' '+ b)
    
        
