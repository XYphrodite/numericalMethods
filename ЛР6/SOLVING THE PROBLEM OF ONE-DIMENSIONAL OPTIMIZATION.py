import math
import matplotlib.pyplot as plt
import numpy as np


def foo(x):
    return 1.35 * math.cos(0.54 * x) + 0.78 * math.pow(x, 2) - 2.06


def find_x(x1, x2, x3, dx):
    return x2 + (dx * (foo(x1) - foo(x3))) / (2 * (foo(x1) - 2 * foo(x2) + foo(x3)))


def optimization(a, b, eps, dx):
    r_dx = dx
    while foo(b - dx) < foo(b):
        if foo(b - 3 * dx) < foo(b):
            b -= dx
        else:
            break
    # y_1 = foo(b - 3 * dx)
    # y_2 = foo(b - 3 / 2 * dx)
    # y_3 = foo(b)
    # y_4 = foo(b + 3 / 2 * dx)
    x_1 = find_x(b - 3 * dx, b - 3 / 2 * dx, b, r_dx)
    x_2 = find_x(b - 3 / 2 * dx, b, b + 3 / 2 * dx, r_dx)
    if math.fabs((foo(x_1) - foo(x_2))) <= eps:
        return x_1
    return optimization(a, b, eps, r_dx / 2)


eps = 0.001
a = -5
b = 5
dx = math.fabs(a) + math.fabs(b) * eps / 100
result = optimization(a, b, eps, dx)
print(f'''x = {round(result, 4)}\ny = {round(foo(result), 4)}''')

plt.figure(figsize=(5, 8))
x = np.linspace(a, b, 50)
y = [foo(i) for i in x]
plt.plot(x, y, 'green')
plt.plot(result, foo(result), 'rp')
plt.title("f(x)")
plt.ylabel('y', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.grid(True)

plt.show()
