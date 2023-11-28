n = int(input())
list = [0, 1, 0]
print('1')
komaki = []
for j in range(0, n-1):
    for i in range(0, len(list)-1):
        komaki.append(list[i]+list[i+1])

    list = [0]+komaki+[0]
    javab = list[1:-1]
    komaki = []
    for z in range(0, len(javab)):
        answer = javab.pop()
        print(answer, end=' ')
    print('')
