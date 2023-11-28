import math


def tedadargham(n):
    c = 0
    while n > 0:
        n = n//10
        c = c+1
    return c


list = []
listaddad = []
for i in range(1, 5000):
    listaddad.append(i)
    b = tedadargham(i)
    list.append(b)
k = int(input())

list.reverse()
listaddad.reverse()
sum = 0
while list != []:
    a = listaddad.pop()
    t = list.pop()
    sum = sum+t
    if sum >= k:
        break
sum
q = sum-k
ss = 10**q
namoosanjavab = math.floor(a//ss)
ssss = namoosanjavab % 10

print(ssss)
