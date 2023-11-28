import math
n = int(input())
list = []
javab = 0
for i in range(0, n):
    m = int(input())
    list.append(m)
sum = sum(list)
average = sum/len(list)
for i in range(0, len(list)):
    a = list.pop()
    if a < average:
        ekhtalef = average-a
        javab += ekhtalef
print(int(javab))
