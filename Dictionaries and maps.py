# Enter your code here. Read input from STDIN. Print output to STDOUT
details = {}
n = int(input())
for s in range(n):
    s = input()
    name, Id = s.split()
    details[name] = Id
for m in range(n):
    try:
        m = input()
        if m in details.keys():
            print(m+'='+details[m])
        else:
            print('Not found')
    except EOFError:
        break
        
        
    
