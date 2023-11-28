n = int(input())
list2 = []
list = []
list3 = []
string = []
sum = ''
x = ''
counter = 0
for i in range(0, n):
    esmha = input()
    list.append(esmha)

for i in list:
    lst = [i[z] for z in range(0, len(i))]
    lst.sort()
    for j in lst:
        sum = sum+j
    for k in sum:
        if x != k:
            counter = counter+1
            x = k
    list3.append(counter)
    sum = ''
    counter = 0

list3.sort()
print(list3[-1])
