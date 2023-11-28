import math
k = -1
t = 0
n = int(input())
m = 2*n
for i in range(1, n+1):
    k = k+1
    if k < (n+1)/2:
        for j in range(1, m+1):
            if j < math.ceil(m/4)+i and j > math.ceil(m/4)-i:
                print('*', end='')
            elif j < math.ceil((3*m)/4)+i and j > math.ceil((3*m)/4)-i:
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')
    else:
        t = t+2
        for j in range(1, m+1):
            if j < math.ceil(m/4)+i-t and j > math.ceil(m/4)-i+t:
                print('*', end='')
            elif j < math.ceil((3*m)/4)+i-t and j > math.ceil((3*m)/4)-i+t:
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')
