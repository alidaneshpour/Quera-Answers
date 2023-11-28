n = input()
print(n)
m = []
h = []
sum = ''
for i in n:
    m.append(i)

c = -1
len = len(m)
for i in range(1, len+1):
    c = c+1
    del m[0]
    if m == []:
        break
    t = m[0]*(i)
    final = m[0:]
    for j in final:
        sum = sum+j
    answer = t+sum
    sum = ''
    print(answer)
