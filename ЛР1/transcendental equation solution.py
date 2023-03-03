import math


def foo(x_, t_):
    return math.pow(math.tan(x_), 2) - t_ * x_


def eligible(c1, c2):
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


def half(a, b, eps, t):
    a1 = a
    a2 = a1
    b1 = b
    b2 = b1
    c1 = (a1 + b1) / 2
    c2 = c1
    while math.fabs(foo(c1, t)) > eps:
        if foo(a1, t) * foo(c1, t) < 0:
            print(c1)
            b1 = c1
            c1 = (a1 + b1) / 2
        else:
            a1 = c1
            c1 = (a1 + b1) / 2
    while math.fabs(foo(c2, t)) > eps:
        if foo(c2, t) * foo(b2, t) < 0:
            print(c2)
            a2 = c2
            c2 = (a2 + b2) / 2
        else:
            b2 = c2
            c2 = (a2 + b2) / 2
    print(c1, " ", c2)
    return eligible(c1, c2)


def sectional(b, a, eps, t):
    a1 = a
    b1 = b
    a2 = b1
    b2 = a1
    while True:
        c1 = b1 - ((foo(b1, t) * (b1 - a1)) / (foo(b1, t) - foo(a1, t)))
        print(c1)
        if math.fabs(foo(c1, t)) < eps:
            print("root = ", c1)
            # return c
            break
        a1 = b1
        b1 = c1
    while True:
        c2 = b2 - ((foo(b2, t) * (b2 - a2)) / (foo(b2, t) - foo(a2, t)))
        print(c2)
        if math.fabs(foo(c2, t)) < eps:
            print("root = ", c2)
            # return c
            break
        a2 = b2
        b2 = c2
    return eligible(c1, c2)


c = 1
d = 2
m = 20
h = (d - c) / m
eps = 0.001
r = 6
print("Введите интервал")
a = float(input("a = "))
b = float(input("b = "))

for i in range(0, 21):
    t = c + i * h
    x_1 = half(a, b, eps, t)
    x_2 = sectional(a, b, eps, t)
    print(i + 1, ") t =", round(t, r), "\t->\tx = ", round(x_1, r), " и ", round(x_2, r))
