import math

eps = 0.001


def foo(x, t):
    return (math.pow(math.tan(x), 2) - t * x)


def half(a, b, eps, t):
    a1 = a
    a2 = a
    b1 = b
    b2 = b
    c1 = (a + b) / 2
    c2 = c1
    while (math.fabs(foo(c1, t)) > eps):
        if foo(a1, t) * foo(c1, t) < 0:
            b1 = c1
            c1 = (a1 + b1) / 2
        else:
            a1 = c1
            c1 = (a1 + b1) / 2
    while (math.fabs(foo(c2, t)) > eps):
        if foo(b2, t) * foo(c2, t) < 0:
            a2 = c2
            c2 = (a2 + b2) / 2
        else:
            b2 = c2
            c2 = (a2 + b2) / 2
    #print(c1, " ", c2)
    if c1 > 0:
        if c2 < 0:
            return c1
        else:
            return min(c1, c2)
    else:
        if c2 > 0:
            return c2
        else:
            return max(c1, c2)


def sword(a, b, eps, t):
    a1 = a
    a2 = a
    b1 = b
    b2 = b
    c1 = (a + b) / 2
    c2 = c1
    while (math.fabs(foo(c1, t)) > eps):
        if foo(a1, t) * foo(c1, t) < 0:
            b1 = c1
            c1 = (a1 + b1) / 2
        else:
            a1 = c1
            c1 = (a1 + b1) / 2
    while (math.fabs(foo(c2, t)) > eps):
        if foo(b2, t) * foo(c2, t) < 0:
            a2 = c2
            c2 = (a2 + b2) / 2
        else:
            b2 = c2
            c2 = (a2 + b2) / 2
    #print(c1, " ", c2)
    if c1 > 0:
        if c2 < 0:
            return c1
        else:
            return min(c1, c2)
    else:
        if c2 > 0:
            return c2
        else:
            return max(c1, c2)

a = 0
b = 0
c = 1
d = 2
m = 20
h = (d - c) / m

print("Введите интервал\na = ")
a = float(input())
print("b = ")
b = float(input())

for i in range(0, m + 1):
    t = c + i * h
    print("t = ", t)
    x = half(a, b, eps, t)
    print("x = ", x)
