def fact(n):
    zarb = 1
    for i in range(1, n+1):
        zarb = zarb*i
    return zarb


def Comb(n, m):
    javab = fact(n)//(fact(m)*fact(n-m))
    return javab


def Calc(n):
    zrb = 1
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            zrb = zrb*Comb(i, j)
        sum = sum+zrb
        zrb = 1
    return sum


n = int(input())
print(int(Calc(n)))
