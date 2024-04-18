def solve_f(f, x):                 
    value=0
    for i in range(0, len(f), 2):
        value += f[i] * (x** f[i+1])
    return (value)

def bisection(f, a, b, E):
    while(True):
        c=(a+b) / 2
        if b-c < E:
            return c
        
        elif solve_f(f, c) <= 0 :
            a = c

        else:
            b = c

def find_interval(f):           
    if solve_f(f,0) < 0: 
        for i in range(100):
            if solve_f(f,i) < 0 and solve_f(f,i+1) >= 0 :
                return i, i+1
            
    else:
        for i in range(0, -100, 1):
            if solve_f(f, i) >= 0 and solve_f(f, i-1) < 0 :
                return i+1, i


f = []
n = int(input("Enter how many terms in the function: "))

for i in range(0, n*2, 2):
    power = int(input("Enter the power of x: "))
    constant = int(input(f"Enter the constant of power {power}: "))
    f.append(constant)
    f.append(power)

E = float(input("Enter the value of Epsilon: "))

a, b = find_interval(f)
root = bisection(f, a, b, E)
print(f"root of the given equation is : {root}")