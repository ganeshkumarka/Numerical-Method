def solve_f (f, x):
    value = 0
    for i in range (0, len(f), 2):
        value += f[i] * (x** f[i+1])
    return value

def false_position(f, a, b, E):
    while (True):
        c = (a* solve_f(f, b) - b*solve_f(f, a)) / (solve_f(f, b) - solve_f(f, a))

        if b-c <= E:
            return c
    
        elif solve_f(f, b) * solve_f(f, c) <= 0:
            a = c
        
        else:
            b = c

def find_interval (f):
    if solve_f(f, 0) < 0:
        for i in range(100):
            if solve_f(f, i) < 0 and solve_f(f, i+1) >= 0:
                return i, i+1
        
    else:
        for i in range (0, -100, 1):
            if solve_f(f, i) > 0 and solve_f(f, i-1) <= 0:
                return i+1, i

#input

f = []

n = int(input("Enter the number of terms in the function: "))

for _ in range (0, n*2, 2):
    power = int (input("Enter the power of x: "))
    coefficient = int (input(f"Enter the coefficient of term with power {power}: "))
    f.append(coefficient)
    f.append(power)

E = float(input("Enter the value of epsilon: "))

a, b = find_interval(f)
root = false_position(f, a, b, E)

print("The root of the given equation is :", root)