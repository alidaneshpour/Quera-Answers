import math
n, x, y = input().split()
n = int(n)
x = int(x)
y = int(y)
c = 0
max1 = math.ceil(n/x)
max2 = math.ceil(n/y)
if n % 2 == 1 and x % 2 == 0 and y % 2 == 0:
    print('-1')
else:
    for i in range(0, max1+1):
        for j in range(0, max2+1):
            if n == x*i+y*j:
                c = c+1
                break
        else:
            continue
        break

    if c != 0:
        print(i, j)
    else:
        print('-1')
