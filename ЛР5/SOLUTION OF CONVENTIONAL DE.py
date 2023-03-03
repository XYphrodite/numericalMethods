import math
import matplotlib.pyplot as plt


def voo(x):
    return math.pow(math.e, -math.cos(x + 1))


def zoo():
    return 1 / 8


def goo(x):
    return 2 * (x - 2)


def Foo(x):
    return voo(x) * zoo()


def find_y(x, y):
    res = []
    for i in range(len(x)):
        res.append(Foo(x[i]) - goo(x[i]) * y[i])
    return res


def foo_a(x, y, h_0, eps):
    N = 0
    x_arr = []
    y_arr = []
    while math.fabs((Foo(x) - goo(x) * y)) > eps:
        x_arr.append(x)
        y_arr.append(y)
        x_2 = x + h_0 / 2
        y_2 = y + h_0 / 2 * (Foo(x) - goo(x) * y)
        y = y + h_0 * (Foo(x_2) - goo(x_2) * y)
        N += 1
        x = x_2
    x_arr.append(x)
    y_arr.append(y)
    return N, x_arr, y_arr


def foo_b(x, y, h_0, N):
    x_arr = []
    y_arr = []
    while N > 0:
        x_arr.append(x)
        y_arr.append(y)
        x_2 = x + h_0 / 2
        y_2 = y + h_0 / 2 * (Foo(x) - goo(x) * y)
        y = y + h_0 * (Foo(x_2) - goo(x_2) * y)
        N -= 1
        x = x_2
    x_arr.append(x)
    y_arr.append(y)
    return x_arr, y_arr


eps = math.pow(10, -3)
h_0 = 0.5
x_0 = 1
b = 6
y_0 = 10

N, x_arr_a, y_arr_a = foo_a(x_0, y_0, h_0, eps)
for i in range(len(x_arr_a)):
    print(f'''{i + 1}) f({round(x_arr_a[i], 4)})\t=\t{round(y_arr_a[i], 4)}''')
h = (b - x_0) / N
print()
x_arr_b, y_arr_b = foo_b(x_0, y_0, h, N)
for i in range(len(x_arr_b)):
    print(f'''{i + 1}) f({round(x_arr_b[i], 4)})\t=\t{round(y_arr_b[i], 4)}''')

x1 = x_arr_a
y1 = y_arr_a
x2 = x_arr_b
y2 = y_arr_b

plt.figure(figsize=(18, 9))
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'gp--')
plt.title("С автоматическим выбором шага — зелёный, с постоянным шагом — красный")
plt.ylabel('y', fontsize=18)
plt.xlabel('x', fontsize=18)
plt.grid(True)
plt.plot(x2, y2, 'rp--')
plt.subplot(1, 2, 2)
plt.plot(x1, find_y(x1, y1), 'gp--')
plt.plot(x2, find_y(x2, y2), 'rp--')
plt.title("С автоматическим выбором шага — зелёный, с постоянным шагом — красный")
plt.ylabel('f(x,y)', fontsize=18)
plt.xlabel('x', fontsize=18)
plt.grid(True)

plt.show()
