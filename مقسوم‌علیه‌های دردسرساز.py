def tma(n):
    c = 0
    m = int((n+2)/2)
    if n > 1:
        for i in range(2, m):
            if n % i == 0:
                c += 1
        return(c+2)
    else:
        return(1)


def ma(n):
    b = []
    bb = [1]
    m = int((n+2)/2)
    if n > 1:
        for i in range(1, m):
            if n % i == 0:
                b.append(i)
        b.append(n)
        return(b)
    else:
        return(bb)


list3 = []
list = []
n = int(input())
for i in range(1, n+1):
    tedad = tma(i)
    list.append(tedad)
    list2 = ma(i)
    sumnahayi = sum(list2)
    list3.append(sumnahayi)

print(sum(list), end=' ')
print(sum(list3))
