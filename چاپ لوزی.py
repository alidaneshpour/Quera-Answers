k = -1
t = 0
m = int(input())
n = 2*m+1
for i in range(1, n+1):
    k = k+1
    if k < (n+1)/2:
        for j in range(1, n+1):
            if j < ((n+1)/2)+i and j > ((n+1)/2)-i:
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')
    else:
        t = t+2
        for y in range(1, n+1):
            if y < ((n+1)/2)+i-t and y > ((n+1)/2)-i+t:
                print('*', end='')
            else:
                print(' ', end='')
        print('\n')
