import math
a, b, l = input().split()
a = int(a)
b = int(b)
l = int(l)
if l % 2 == 0:
    t = (a+b)*(l/2)
else:
    y = math.floor((l/2))
    t = (a+b)*y+a
print(int(t))
