# Simpson's 3/8 rule

def simpson3_8 (x, y):
  h = x[1] - x[0]
  middle_term_3, middle_term_2 = 0, 0

  for i in range (1, len(y)-1):
    if i%3 != 0:
      middle_term_3 += y[i]
    else:
      middle_term_2 += y[i]

  result = ((3*h)/8) * (y[0] + 3*middle_term_3 + 2*middle_term_2 + y[len(y)-1])
  return result

x = list(map(float, input("Enter values of x (space separated): ").split()))
y = list(map(float, input("Enter values of y (space separated): ").split()))

print("The Integral is: ", simpson3_8(x, y))