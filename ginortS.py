# Enter your code here. Read input from STDIN. Print output to STDOUT
s = str(input())
low = []
up = []
odd = []
even = []
for i in s:
    if i.islower():
        low.append(i)
    if i.isupper():
        up.append(i)
    if i.isdigit():
        if int(i)%2 != 0:
            odd.append(i)
        if int(i)%2 == 0:
            even.append(i)
print(''.join(sorted(low) + sorted(up) + sorted(odd) + sorted(even)))
