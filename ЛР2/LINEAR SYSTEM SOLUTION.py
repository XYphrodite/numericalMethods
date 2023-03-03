import math

import numpy


def myseidel(A, B, eps):
    n = len(A)
    x = numpy.zeros(n)
    for i in range(n):
        x[i] = A[i][i] / B[i]
    print(x)
    while True:
        x_new = numpy.copy(x)
        for i in range(n):
            s1 = 0
            for j in range(i):
                s1 += A[i][j] * x_new[j]
            s2 = 0
            for j in range(i + 1, n):
                s2 += A[i][j] * x[j]
            x_new[i] = (B[i] - s1 - s2) / A[i][i]
        print(x_new)
        sum = 0
        for i in range(n):
            sum += (x_new[i] - x[i]) ** 2
        if numpy.sqrt(sum) <= eps:
            return x_new
        x = x_new


matrix_txt = open('matrix.txt', 'r')
matrix = matrix_txt.read()
matrix_txt.close()
eps = 0.001
print(matrix)
rows, columns = (5, 6)
matrix_list = []
matrix_line = []
word = ''
for i in matrix:
    if i in ' \t\n':
        matrix_line.append(float(word))
        word = ''
        if len(matrix_line) == 6:
            matrix_list.append(matrix_line)
            matrix_line = []
    else:
        word += i

A = []
A_line = []
B = []
for i in range(0, 5):
    for j in range(0, 6):
        if j == 5:
            B.append(matrix_list[i][j])
            A.append(A_line)
            A_line = []
        else:
            A_line.append(matrix_list[i][j])

X = myseidel(A, B, eps)
a = 1
for i in X:
    print(f'''x{a} = {round(i, 4)}''')
    a += 1
