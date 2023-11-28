n = input()
r = 0
y = 0
g = 0
ff = 0
ttt = 0
for i in n:
    if i == 'R':
        r = r+1
    elif i == 'Y':
        y = y+1

if r > 2 and y < 2:
    print("nakhor lite")
    ff = 1
    ttt = 1

if r > 1 and y > 1:
    print("nakhor lite")
    ff = 1
    ttt = 1

if r+y == 5 and ttt == 0:
    print("nakhor lite")
    ff = 1

if ff == 0:
    print("rahat baash")
