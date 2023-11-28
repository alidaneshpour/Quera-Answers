n = int(input())
list = list(map(int, input().split()))
ss = 0
list2 = []
s = sum(list)
list.reverse()
for i in range(0, len(list)):
    a = list.pop()
    ss = ss+a
    list2.append(ss)

list2.sort()
aa = list2[-1]
if aa < 0:
    print('0')
else:
    print(aa)
