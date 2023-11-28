n = int(input())
list = list(map(int, input().split()))
# list = [5465, 51, 168, 48, 5616, 52, 54, 4, 64, 984, 98, 651, 65, 46, 54, 9489, 5, 65, 468, 46, 46, 465, 454, 654, 654, 654, 6, 54, 5645, 5, 5, 45, 54654, 54564, 654, 54654, 656465, 545465, 5, 54, 64, 54654, 54, 54544, 54, 554, 9879, 8556, 56, 64, 4, 646, 464, 9, 54, 656, 54, 546, 46, 5, 45, 5646, 65, 45789, 79898, 879, 98, 8, 8489, 4984, 984, 89, 46, 4, 9498, 48, 49, 49, 654, 654, 6, 48, 49, 4, 54656, 564, 654, 5, 556, 456, 45, 45, 4, 654, 5, 54, 6, 54, 64, 6, 4, 564, 64, 56, 46, 4, 6487, 97, 9, 564, 64, 65, 4894, 984, 64, 98, 498, 498, 4, 98, 4, 4, 64, 9, 64, 984, 98, 4, 84, 9, 486, 6, 542, 54, 6546, 4, 54, 54, 654, 6, 4, 654, 65, 465, 65, 4, 65, 465, 98, 789, 59, 548, 4, 94, 98, 4, 984, 98, 4, 984, 98, 48, 5, 165, 46, 46, 84, 86, 4, 84, 69, 41, 641, 6, 4, 68, 416, 84, 84, 9849849, 4, 98, 49, 4, 94, 98, 49, 84, 94, 98, 46, 5465, 4, 54, 65, 465, 456, 56, 465, 46, 548, 798, 798, 798, 498, 498, 489, 498, 498, 468, 468, 4, 64, 8, 498, 49, 84, 984, 9849, 84, 94, 984, 98, 48, 4984, 8798, 465, 1563, 16, 516, 6, 16, 84, 684, 98648, 949, 8498, 4, 984, 98, 496]
dorraft = []
dorbargasht = []
answer = []


c = 0
for i in list:
    koochiknadashtan = 0
    c = c+1
    list2 = list[c:]
    t = c
    for j in list2:
        t = t+1
        if j < i:
            dorraft.append((t-c-1))
            koochiknadashtan = 1
            break
    if koochiknadashtan == 0:
        dorraft.append(len(list)-c)


list.reverse()
c = 0
for i in list:
    koochiknadashtan = 0
    c = c+1
    list2 = list[c:]
    t = c
    for j in list2:
        t = t+1
        if j < i:
            dorbargasht.append((t-c-1))
            koochiknadashtan = 1
            break
    if koochiknadashtan == 0:
        dorbargasht.append(len(list)-c)

dorbargasht.reverse()
list.reverse()
for i in range(0, len(list)):
    sum = dorraft[i]+dorbargasht[i]+1
    masahat = sum*list[i]
    answer.append(masahat)

answer.sort()
print(answer[-1], len(list))
