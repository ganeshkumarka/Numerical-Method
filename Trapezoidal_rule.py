def trapezoidal (x, y):
  h = x[1] - x[0]
  middle_term = 0

  for i in range(1, len(y)-1):
    middle_term += y[i]

  result = (h/2) * (y[0] + 2*middle_term + y[len(y)-1])
  return result

x = list(map(float, input("Enter values of x (space separated): ").split()))
y = list(map(float, input("Enter values of y (space separated): ").split()))

print ("The integral is: ", trapezoidal(x, y))