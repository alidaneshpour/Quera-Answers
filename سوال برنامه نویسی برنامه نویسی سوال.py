n = int(input())
list = list(map(str, input().split()))

for i in range(0, len(list)):
    a = list.pop()
    print(a, end=" ")
