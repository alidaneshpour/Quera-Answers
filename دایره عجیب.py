n, k = input().split()
n = int(n)
k = int(k)
c = 0
sum = 1
nn = 0
list = []
for i in range(1, n+1):
    list.append(i)
# print(list)

while list[sum] != 1:
    if nn == 0:
        sum = 0
        nn = 1
    sum = sum+k
    sum = sum % n
    c = c+1
    nn = 2

print(c)
