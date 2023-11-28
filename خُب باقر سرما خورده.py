n1 = input()
n2 = input()
n3 = input()
n4 = input()
n5 = input()

c = 0
if ('MOLANA' in n1) == True or ('HAFEZ' in n1) == True:
    print("1", end=' ')
    c = 1

if ('MOLANA' in n2) == True or ('HAFEZ' in n2) == True:
    print("2", end=' ')
    c = 1

if ('MOLANA' in n3) == True or ('HAFEZ' in n3) == True:
    print("3", end=" ")
    c = 1

if ('MOLANA' in n4) == True or ('HAFEZ' in n4) == True:
    print("4", end=' ')
    c = 1

if ('MOLANA' in n5) == True or ('HAFEZ' in n5) == True:
    print("5", end=" ")
    c = 1

if c == 0:
    print('NOT FOUND!')
