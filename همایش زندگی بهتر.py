r, c = input().split()
r = int(r)
c = int(c)
if c > 10:
    a = 'Left'
    d = 21-c
else:
    a = 'Right'
    d = c
b = 11-r

print(a, b, d)
