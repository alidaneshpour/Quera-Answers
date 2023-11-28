n = int(input())
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

if sum == kk:
    print('YES')
else:
    print('NO')
