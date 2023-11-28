import math


def baraks(n):
    n = int(n)
    kk = n
    m = []
    b = []
    sum = 0
    while n != 0:
        t = n % 10
        m.append(t)
        n = n//10

    s = len(m)

    for i in range(1, s+1):
        b = m.pop()
        sum = sum+b*(10**(i-1))
    return(sum)


c = 0
sum1 = 0
k = int(input())
ramz = int(input())
baraksadad = baraks(ramz)
for i in range(1, k+1):
    m = int(input())
    c = 0
    test = False
    while test == False:
        ramzyekraghami = baraksadad % 10
        emtehan = m % 10
        m = math.floor(m/10)
        c += 1
        if emtehan == ramzyekraghami:
            test = True
    baraksadad = math.floor(baraksadad/10)
    if c > 4:
        c = 9-c
    sum1 = sum1+c
print(sum1)
