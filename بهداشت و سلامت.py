x = int(input())
n = int(input())
if n == 0:
    print('20')
elif n == 7:
    print(x)
else:
    k = x-n
    if k > -0.5:
        print(k)
    else:
        print('0')
