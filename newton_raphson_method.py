from sympy import *
import random

def newton_raphson(f, x0, E, itmax, ier):
    itnum = 1

    while True:
        df = diff(f, x)

        denom = df.subs(x, x0)

        if denom == 0:
            ier = 2
            return 0, ier

        x1 = x0 - (f.subs(x, x0)/denom)

        if abs(x1 - x0) <= E:
            ier = 0
            root = x1
            return root, ier

        elif itnum == itmax:
            ier = 1
            return x1, ier

        else:
            itnum += 1
            x0 = x1

function = input("Enter the function: ").replace(' ', '')
x = symbols('x')
f = sympify(function)

a = eval(input("Enter the interval a: "))
b = eval(input("Enter the interval b: "))

print("The interval range is: [", a, ", ", b, "]")

x0 = random.uniform(a, b)
E = float(input("Enter the value of absolute error: "))

root, ier = newton_raphson(f, x0, E, 30, 0)

if ier == 2:
    print("Derivative is 0..!")
elif ier == 1:
    print("Maximum number of iterations reached..")
    print("The root is: ", root)
else:
    print("The root is: ", root)