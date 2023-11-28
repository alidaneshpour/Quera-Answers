n, m = input().split()
n = int(n)
m = int(m)
c = 0
for i in range(0, n):
    h = input()
    for j in h:
        if j == '*':
            c = c+1

print(c)
