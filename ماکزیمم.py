n = int(input())
list = list(map(int, input().split()))


b = 0
for j in range(1, len(list)+1):
    a = list.pop()
    if a > b:
        b = a

print(b)
