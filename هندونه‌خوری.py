n = int(input())
list = list(map(int, input().split()))
max = 0
list2 = []
for i in range(0, len(list)):
    a = list.pop()
    list2.append(a)
    if a > max:
        max = a

list2.reverse()
c = len(list2)
for i in range(0, len(list2)):
    t = list2.pop()
    if t == max:
        break
    c = c-1

print(c)
