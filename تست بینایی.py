n = int(input())
s = input()
p = input()
c = -1
g = 0
for i in s:
    c = c+1
    if i != p[c]:
        g = g+1

print(g)
