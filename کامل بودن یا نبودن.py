n = int(input())
b = []
bb = [1]
m = int((n+2)/2)
if n > 1:
    for i in range(2, m):
        if n % i == 0:
            b.append(i)

a = sum(b)+1
if a == n:
    print('YES')
else:
    print('NO')
