sum = 0
m, s = input().split()
m = int(m)
s = int(s)
ss = s
# while m > 100 and m < 1 or s > 900 and s < 0:
#     m = int(input())
# while s > 900 and s < 0:
#     s = int(input())
if s > m*9 or s < 0:
    print('-1 -1')
if s == 0 and m == 1:
    print('0 0')
if s > 0:
    if s < m*9 or s == m*9:
        a = int(s/9)
        b = s % 9
        c = 10**(m-1)
        if b == 0:
            eee = 10**(a-1)
        else:
            eee = 10**a
        for salam in range(0, 100):
            if s < 9 or s == 9:
                sum = sum+s*(10**salam)
                break
            s = s-9
            sum = sum+9*(10**salam)

        if sum > c:
            f = sum
        else:
            f = sum+c-eee
        if ss == m*9:
            print(f, 10**m-1)
        else:
            g = (10**m)-1
            eeeee = (10**abs((m-a-1)))
            h = int(g//eeeee)
            if h % 10 == 0:
                h = h-1
            i = abs(h-9+b)
            j = '0'*(m-a-1)
            p = str(i)
            k = p+j
            w = int(k)
            print(f, w)
elif m > 0:
    print('-1 -1')
