import re;

N = int(input())
for i in range(N):
    try:
        re.compile(input())
        Output = True
    except re.error:
        Output = False
    
    print(Output)
