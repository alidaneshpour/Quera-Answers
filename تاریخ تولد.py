import math
n = input()
c = -1
s1 = ''
s2 = ''
for i in n:
    c = c+1
    if c < 2:
        s1 = s1+i
    if c > 1:
        s2 = s2+i

print(f"saal:{s1}")
print(f"maah:{s2}")
