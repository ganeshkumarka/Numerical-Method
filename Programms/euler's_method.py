def euler(f, x0, y0, target_x, h):
  x = x0
  y = y0

  while x < target_x:
    y += h*f(x,y)
    x += h

  return y

def f(x,y):
  return (y-x)/(y+x)

x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
target_x = float(input("Enter target x: "))
h = float(input("Enter value of h: "))

print("The value of y at x=", target_x, " is: ", euler(f,x0,y0,target_x,h))