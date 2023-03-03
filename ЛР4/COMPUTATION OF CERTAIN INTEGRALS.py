import math
import matplotlib.pyplot as plt
import numpy as np


def foo_1(x):
    return 1 / (1 + math.sqrt(x))


def voo(z):
    return (math.pow(math.e, 2 * z) - 1) / (math.pow(math.e, 2 * z) + 1)


def zoo(x):
    return (2 - 3 * x) / (4 + math.pow(x, 2))


def get_t_i(c, h, m):
    t_i = []
    for i in range(0, m + 1):
        t_i.append(c + i * h)
    return t_i


def foo_2(x, t):
    z = t / (1 + math.pow(x, 2)) + u * x
    return voo(z) * zoo(x)


def gaus_1(a, b, n, a_i, t_i):
    f_ = (b - a) / 2
    sum_ = 0
    for i in range(n):
        sum_ += a_i[i] * foo_1((b + a) / 2 + (b - a) / 2 * t_i[i])
    return f_ * sum_


def gaus_2(a, b, n, a_i, t_i, t):
    res = []
    for i in range(len(t)):
        f_ = (b - a) / 2
        sum_ = 0
        for j in range(n):
            sum_ += a_i[j] * foo_2(((b + a) / 2 + (b - a) / 2 * t_i[j]), t[i])
        res.append(f_ * sum_)
    return res


a_1 = 0
b_1 = 4
u = 0.05
a_2 = math.pi / 4
b_2 = 3 * math.pi / 4
c = 1
d = 2.5
m = 15
h = (d - c) / m
t_i = get_t_i(c, h, m)
A_i = [0.10122854, 0.22238104, 0.31370664, 0.36268378, 0.36268378, 0.31370664, 0.22238104, 0.10122854]
t_i_1 = [-0.96028986, -0.79666648, -0.52553242, -0.18343464, 0.18343464, 0.52553242, 0.79666648, 0.96028986]
n = len(t_i_1)
foo_1_res = gaus_1(a_1, b_1, n, A_i, t_i_1)
print(f'''u = {round(foo_1_res, 5)}''')
foo_2_res = gaus_2(a_2, b_2, n, A_i, t_i_1, t_i)
for i in range(len(foo_2_res)):
    print(f'''{i + 1}) F({round(t_i[i], 1)}) = {round(foo_2_res[i], 4)}''')

x = t_i
y = foo_2_res
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y, 'p--')
plt.title("F(t)")
plt.ylabel('y', fontsize=18)
plt.xlabel('t', fontsize=18)
plt.grid(True)

plt.subplot(1, 2, 2)
x = np.linspace(a_1, b_1, 100000)
y = [foo_1(i) for i in x]
plt.plot(x, y, 'r')
plt.grid(True)
plt.ylabel('y', fontsize=18)
plt.xlabel('x', fontsize=18)
plt.title("y = 1 / (1 + sqrt(x))")
plt.show()
