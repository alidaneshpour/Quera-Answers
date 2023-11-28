import timeit
start = timeit.default_timer()
n = int(input())
m = int(n/2)+1
mm = int(n/4)
c = 0
cc = 0
if n % 2 == 1:
    print('Impossible')
else:
    for i in range(mm, m):
        if c == 1:
            break
        had = n-i
        had2 = int(had/2)+1
        had3 = int(had2/2)-1
        for j in range(had3, had2):
            if j > i:
                break
            if j >= int(had/2):
                z = had-j
                if i**2 == z**2+j**2:
                    cc = cc+1
                    if z > j:
                        j, z = z, j
                    if cc == 1:
                        print(z, j, i)
                        c = c+1
    if c == 0:
        print('Impossible')

stop = timeit.default_timer()
print('time: ', stop-start)
