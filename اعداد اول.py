def addadaval(n):
    c = 0
    m = int(n/2)+2
    if n == 2:
        return n
    elif n != 1:
        for i in range(2, m):
            if n % i == 0:
                c = c+1
        if c == 0:
            return n


answer = []
a = int(input())
b = int(input())
if a > b:
    z = b
    b = a
    a = z
for i in range(a, b+1):
    answer.append(addadaval(i))

answer.reverse()
tool = len(answer)
for i in range(0, tool):
    d = answer.pop()
    if d != None:
        print(d)
