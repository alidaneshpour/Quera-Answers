a = int(input())
b = input()
c = int(input())
d = input()
e = int(input())
f = input()
b = b.split(" ")
d = d.split(" ")
f = f.split(" ")
g = b+d+f
r0, r1, r2, r3, r4, r5, r6 = 0, 0, 0, 0, 0, 0, 0
for i in range(1, 25):
    z = g.pop()
    # print(g)
    if z == "shanbe":
        r0 = 1
    if z == "1shanbe":
        r1 = 1
    if z == "2shanbe":
        r2 = 1
    if z == "3shanbe":
        r3 = 1
    if z == "4shanbe":
        r4 = 1
    if z == "5shanbe":
        r5 = 1
    if z == "jome":
        r6 = 1
    if g == []:
        break

r7 = r0+r1+r2+r3+r4+r5+r6
#print(r0, r1, r2, r3, r4, r5, r6, 7-r7)
print(7-r7)
