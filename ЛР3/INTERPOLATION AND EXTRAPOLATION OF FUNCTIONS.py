import math
import matplotlib.pyplot as plt


def nice_table(t):
    res = ''
    for i in range(len(t)):
        for j in range(len(t[i])):
            res += str(round(t[i][j],8)) + '\t'
        res += '\n'
    return res


def load_data(path):
    file = open(path, 'r')
    data = file.read()
    file.close()
    x_i = []
    y_i = []
    x_j = []
    table = []
    digit = ''
    for i in range(len(data)):
        if data[i] not in ' \n':
            digit += data[i]
        else:
            if digit != '':
                table.append(float(digit))
                digit = ''
    if digit != '':
        table.append(float(digit))
    for i in range(len(table)):
        if i < 15:
            if i % 3 == 0:
                x_i.append(table[i])
            elif i % 3 == 1:
                y_i.append(table[i])
            else:
                x_j.append(table[i])
        else:
            if i % 2 == 1:
                x_i.append(table[i])
            else:
                y_i.append(table[i])
    return x_i, y_i, x_j


def get_D_table(y_i):
    if len(y_i) > 1:
        new_y_i = []
        for i in range(len(y_i) - 1):
            new_y_i.append(y_i[i + 1] - y_i[i])
        d.append(y_i)
        return get_D_table(new_y_i)
    return y_i


def find_h(x_i):
    return x_i[1] - x_i[0]


def get_a_i(t, h):
    a_i = []
    for i in range(len(t[0])):
        a = t[i][len(t[i]) - 1] / (math.factorial(i) * pow(h, i))
        a_i.append(a)
    # print(a_i)
    return a_i


def newton(x_i, x, a_i):
    y = 0
    for i in range(0, len(a_i)):
        if i == 0:
            y = a_i[i]
        else:
            s = 1
            for k in range(0, i):
                s *= (x - x_i[len(x_i) - 1 - k])
            y += a_i[i] * s
    return y


def interpolation(x_i, y_i, x_j, t):
    h = find_h(x_i)
    a_i = get_a_i(t, h)
    y_j = []
    for i in range(len(x_j)):
        y_j.append(newton(x_i, x_j[i], a_i))
    return y_j


d = []
path = 'data.txt'
x_i, y_i, x_j = load_data(path)
d.append(get_D_table(y_i))
print(nice_table(d))
result = interpolation(x_i, y_i, x_j, d)
for i in range(len(x_j)):
    print(f'''{i + 1}) x_j = {x_j[i]}\tf(x_j) = {result[i]}''')

plt.figure(figsize=(12, 8))
plt.plot(x_i, y_i, 'gp--')
plt.title("y = f(x_i) — зелёный, и f(x_j) — красный", fontsize=20)
plt.grid(True)
plt.plot(x_j, result, 'rp')
plt.ylabel('y', fontsize=18)
plt.xlabel('x', fontsize=18)
plt.show()
