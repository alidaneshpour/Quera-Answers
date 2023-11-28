import math
sum = 0
n = int(input())
for i in range(1, 10000):
    m = n % 10
    n = math.floor(n//10)
    sum = sum+m
    #print(m, n, sum)
    if n == 0 and sum < 10:
        print(sum)
        break
    elif n == 0:
        n = sum
        sum = 0
