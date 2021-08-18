# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())
ac = (ab**2 + bc**2)**(1/2)
a = bc/2
mc = ac/2
phi = math.degrees(math.acos(a/mc))
print(int(round(phi)), chr(176), sep = '')
