a = []
for i in range(1, 10000):
    n = int(input())
    if n == 0:
        break
    a.append(n)

for i in range(1, 10000):
    if a == []:
        break
    b = a.pop()
    print(b)
