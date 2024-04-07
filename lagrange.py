def lagrange(x, y, value):
    result = 0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if j != i:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    return result

x = list(map(float, input("Enter the values of x (space-separated): ").split()))
y = list(map(float, input("Enter the values of y (space-separated): ").split()))

value = float(input("Enter the intermediate value to be found: "))

interpolated_value = lagrange(x, y, value)

print("Interpolated value:", interpolated_value)