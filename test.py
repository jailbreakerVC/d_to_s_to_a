def sumOfRow(A, row):
    sum = 0
    for i in range(0, len(A[row])):
        sum = sum + A[row][i]
    return sum


def Sumofelementsinacolumn(A, column):
    sum = 0
    for i in range(0, len(A)):
        sum += A[i][column]
    return sum


def solution():
    A = [[2, 7, 5], [3, 1, 1], [2, 1, -7], [0, 2, 1], [1, 6, 8]]
    N = len(A)
    M = len(A[0])
    product = M*N
    equlib = [[]]
    points = 0
    for i in range(0, product):
        for j in range(0, N):
            for k in range(0, M):
                if sumOfRow(A, j) == Sumofelementsinacolumn(A, k):
                    equlib.append([j, k])

    print(len(equlib))


solution()
