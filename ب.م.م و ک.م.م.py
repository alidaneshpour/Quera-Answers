from itertools import product
import math


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


answer = []
javab = []
tavanha1 = []
tavanha2 = []
edame = []
c = 0
counter = 0
p = 1
zarb = 0
q = 1
cccc = 0
n, m = input().split()
n = int(n)
m = int(m)
for shomarande in range(1, 3):
    if shomarande == 1:
        a = n
        b = 1
    else:
        a = m
        b = 1
    for i in range(1, a+1):
        if addadaval(i) != None:
            answer.append(addadaval(i))
            if shomarande == 1:
                c = c+1

avalha1 = answer[c:]
avalha2 = answer[:c]
n1 = n
m1 = m
if n1 > m1:
    n1, m1 = m1, n1
for i in range(0, len(avalha2)):
    while n % avalha2[i] == 0:
        counter += 1
        n = n//avalha2[i]
    n = n1
    tavanha1.append(counter)
    counter = 0

counter = 0
for i in range(0, len(avalha1)):
    while m % avalha1[i] == 0:
        counter += 1
        m = m//avalha1[i]
    m = m1
    tavanha2.append(counter)
    counter = 0

if sum(tavanha1) == 0:
    tavanha1 = tavanha1+[n]

if sum(tavanha2) == 0:
    tavanha2 = tavanha2+[m]

if len(tavanha1) > len(tavanha2):
    for i in range(0, len(tavanha2)):
        zarb = avalha1[i]**min(tavanha2[i], tavanha1[i])
        p = p*zarb
    for i in range(0, len(tavanha2)):
        zarb1 = avalha1[i]**max(tavanha2[i], tavanha1[i])
        cccc = cccc+1
        q = q*zarb1
    eee = len(tavanha2)
    edame = tavanha1[eee:]
    for i in range(cccc, len(tavanha1)-1):
        zarb1 = avalha1[i]**tavanha1[i]
        q = q*zarb1


else:
    for i in range(0, len(tavanha1)):
        zarb = avalha1[i]**min(tavanha2[i], tavanha1[i])
        p = p*zarb
    for i in range(0, len(tavanha1)):
        # if tavanha2[i] != 0 and tavanha1[i] != 0:
        zarb1 = avalha1[i]**max(tavanha2[i], tavanha1[i])
        q = q*zarb1


print(answer, avalha1, avalha2, tavanha1, tavanha2, p, q)
