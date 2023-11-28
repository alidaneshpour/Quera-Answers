n = int(input())
m = int(input())
k = n
kk = m
c = 0
for i in range(1, 4):
    r = n % 10
    p = m % 10
    n = n/10
    m = m/10
    if r < p:
        print(f"{k} < {kk}")
        c = 1
        break
    if p < r:
        print(f"{kk} < {k}")
        c = 1
        break

if c != 1:
    print(f"{kk} = {k}")
