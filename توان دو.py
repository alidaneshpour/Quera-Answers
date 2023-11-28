n = int(input())
for i in range(0, 10**9):
    if n < (2**i):
        print(2**i)
        break
