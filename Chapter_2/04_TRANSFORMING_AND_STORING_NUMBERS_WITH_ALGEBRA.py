# Exercise 1 solving first-degree equation
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def equation(a,b,c,d):
    return (d-b)/(a-c)


# Exercise 2 quadratic formula


def quad(a, b, c):
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10


def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =", x)
        x += 1
    print("done.")

x = np.arange(-10, 10, 0.1)
y = 6*x**3 + 31*x**2 + 3*x - 10

plt.plot(x,y)
plt.show()
print(equation(12, 18, -34, 67))
print(equation(1/2, 2/3, 1/5, 7/8))
print(quad(2,7,-15))
plug()
