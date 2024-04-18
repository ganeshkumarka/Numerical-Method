import numpy as np

def f(x, function):
  return eval(function)
  

def mullers(x0,x1,x2,E):

  iteration = 0

  while True:
    iteration += 1
    h0 = x1 - x0
    h1 = x2 - x1

    d0 = (f(x1, function) - f(x0, function)) / h0
    d1 = (f(x2, function) - f(x1, function)) / h1

    a = (d1 - d0) / (h1 + h0)
    b = a * h1 + d1
    c = f(x2, function)

    denom = b**2 - 4 * a * c

    if denom == 0:
      print("Error..! Division by zero..")
      return None

    x3 = x2 - ((2*c) / (b + np.sqrt(denom)))

    if np.abs((x3-x2)/x3) * 100 <= E or iteration >= 100:
      break


    x0 = x1
    x1 = x2
    x2 = x3

  return x3, iteration

function = input("Enter the function: ").replace(' ', '')
x0 = float(input("Enter the first guess: "))
x1 = float(input("Enter the second guess: "))
x2 = float(input("Enter the third guess: "))

E = float(input("Enter the error: "))

root, iteration = mullers(x0, x1, x2, E)
print("The root is: ", root)
print("The number of iterations taken is: ", iteration)