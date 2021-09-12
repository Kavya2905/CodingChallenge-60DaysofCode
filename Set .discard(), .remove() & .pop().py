n = int(input())
s = set(map(int, input().split()))
 
for i in range(int(input())):
    m = input().split()
    if m[0] =='pop':
        s.pop()
    elif m[0] =='remove':
        s.remove(int(m[1]))
    else:
        s.discard(int(m[1]))
print(sum(s))
