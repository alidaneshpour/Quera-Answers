n, m = input().split()
n = int(n)
m = int(m)
mazrab = 0
mazrab1 = 0
if n < m:
    mazrab = m-n
    javab1 = 'R'*mazrab
    print(javab1)
elif m == n:
    print('Saal Noo Mobarak!')
else:
    mazrab1 = n-m
    javab2 = 'L'*mazrab1
    print(javab2)
