# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
# list3 = list(map(int, input().split()))
# list4 = list(map(int, input().split()))
# list5 = list(map(int, input().split()))
# list6 = list(map(int, input().split()))
# list7 = list(map(int, input().split()))
# list8 = list(map(int, input().split()))
# list9 = list(map(int, input().split()))

# m = int(input('number of rows, m : '))
# n = int(input('number of columns, n : '))
# a = []
# for i in range(1, m+1):
#     b = []
#     print("{0} Row".format(i))
#     for j in range(1, n+1):
#         b.append(int(input("{0} Column: " .format(j))))
#     a.append(b)
# print(a)

# listasli = []
# list1 = []
# listamoodi = []
# for i in range(0, 9):
#     list1 = list(map(int, input().split()))
#     listasli.append(list1)
# print(listasli)
# print(listasli[1][4])
# listamoodi = listasli[:]
# for i in listasli:
#     print(i)
#     for j in range(0, 9):
#         if j == 0:
#             listamoodi[j] = i[j]
#         if j == 1:
#             listamoodi[j] = i[j]
#         if j == 2:
#             listamoodi[j] = i[j]
#         if j == 3:
#             listamoodi[j] = i[j]
#         if j == 4:
#             listamoodi[j] = i[j]
#         if j == 5:
#             listamoodi[j] = i[j]
#         if j == 6:
#             listamoodi[j] = i[j]
#         if j == 7:
#             listamoodi[j] = i[j]
#         if j == 8:
#             listamoodi[j] = i[j]

# print(listamoodi)

M = 9


def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


# puzzle([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#         [5, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 8, 7, 0, 0, 0, 0, 3, 1],
#         [0, 0, 3, 0, 1, 0, 0, 8, 0],
#         [9, 0, 0, 8, 6, 3, 0, 0, 5],
#         [0, 5, 0, 0, 9, 0, 6, 0, 0],
#         [1, 3, 0, 0, 0, 0, 2, 5, 0],
#         [0, 0, 0, 0, 0, 0, 0, 7, 4],
#         [0, 0, 5, 2, 0, 6, 3, 0, 0]])


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def Suduko(grid, row, col):

    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


'''0 means the cells where no value is assigned'''
# grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#         [5, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 8, 7, 0, 0, 0, 0, 3, 1],
#         [0, 0, 3, 0, 1, 0, 0, 8, 0],
#         [9, 0, 0, 8, 6, 3, 0, 0, 5],
#         [0, 5, 0, 0, 9, 0, 6, 0, 0],
#         [1, 3, 0, 0, 0, 0, 2, 5, 0],
#         [0, 0, 0, 0, 0, 0, 0, 7, 4],
#         [0, 0, 5, 2, 0, 6, 3, 0, 0]]
# grid = []
# for i in range(0, 9):
#     list1 = list(map(int, input().split()))
#     grid.append(list1)

# if (Suduko(grid, 0, 0)):
#     puzzle(grid)
# else:
#     print("Solution does not exist:(")
