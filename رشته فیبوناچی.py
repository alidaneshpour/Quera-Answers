n = int(input())
a1 = 1
a2 = 2
an = 0
c = 0
jaygozin = []
adadfibo = []
while an < n:
    an = a1+a2
    adadfibo.append(an)
    a1 = a2
    a2 = an
    adadfiboasli = [1]+[2]+adadfibo
    tt = len(adadfiboasli)
for j in range(1, n+1):
    for i in range(0, tt):
        pop = adadfiboasli.pop()
        jaygozin.append(pop)
        if j == pop:
            print("+", end='')
            c = 0
            c = c+1
    if c == 0:
        print('-', end='')

    adadfiboasli = jaygozin
    jaygozin = []
    c = 0
