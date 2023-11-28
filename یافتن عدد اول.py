def addadaval(n):
    c = 0
    m = int(n/2)+2
    if n == 2:
        return n
    elif n != 1:
        for i in range(2, m):
            if n % i == 0:
                c = c+1
        if c == 0:
            return n


def majmoeargham(n):
    n = int(n)
    sum = 0
    import math
    while n > 0:
        s = n % 10
        n = math.floor(n//10)
        sum = sum+s
    return sum


n = int(input())
b = majmoeargham(n)
list = []
for i in range(n+1, 1000000):
    dd = addadaval(i)
    if dd != None:
        list.append(dd)
        if len(list) > b-1:
            break

print(list[-1])
