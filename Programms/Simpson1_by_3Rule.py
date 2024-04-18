def simpson1_3(x, y):
  h = x[1] - x[0]
  middle_term_4, middle_term_2 = 0, 0
  for i in range (1, len(y)-1, 2):
    middle_term_4 += y[i]
  for i in range (2, len(y)-1, 2):
    middle_term_2 += y[i]
  result = (h/3) * (y[0] + 4*middle_term_4 + 2*middle_term_2 + y[len(y)-1])
  return result

x = list(map(float, input("Enter the values of x(space separated): ").split()))
y = list(map(float, input("Enter the values of y(space separated): ").split()))

print("The Integral is: ", simpson1_3(x, y))