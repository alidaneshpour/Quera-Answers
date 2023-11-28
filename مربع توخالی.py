a = int(input())
b = int(input())
if b > a or b == a:
    print('Wrong order!')
elif (b-a) % 2 == 1:
    print('Wrong difference!')
else:
    for i in range(1, a+1):
        for j in range(1, a+1):
            if i < ((a-b)/2)+1 or j < ((a-b)/2)+1 or i > (a-(a-b)/2) or j > (a-(a-b)/2):
                print('*', end=" ")
            else:
                print(' ', end=" ")
        print('\n')
