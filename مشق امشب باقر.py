m, s, t = input().split()
m = int(m)
s = int(s)
t = int(t)
sum = m+s+t
if s == 0 or t == 0 or m == 0:
    print('No')
else:
    if sum == 180:
        print('Yes')
    else:
        print('No')
