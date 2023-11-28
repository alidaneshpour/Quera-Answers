n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

a = []
sum = n1+n2+n3+n4
average = sum/4
product = n1*n2*n3*n4
list = [n1, n2, n3, n4]
list.sort()
max = list[-1]
min = list[0]

print(f"Sum : {'%.6f' % sum}")
print(f"Average : {'%.6f' % average}")
print(f"Product : {'%.6f' % product}")
print(f"MAX : {'%.6f' % max}")
print(f"MIN : {'%.6f' % min}")
