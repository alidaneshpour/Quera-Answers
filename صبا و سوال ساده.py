import math
n, k = input().split()
n = int(n)
k = int(k)
for i in range(0, k):
    n = n/2
b = math.floor(n)
print(b)
