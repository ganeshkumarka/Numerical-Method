def ForwardInterpolation(x, y, value):
    if value < x[0] or value > x[-1]:
        print("Given value is not intermediate..!")
        return None

    h = x[1] - x[0]
    p = (value - x[0]) / h

    diff = [y]
    result = y[0]
    for i in range(1, len(x)):
        diff.append([])
        for j in range(len(x) - i):
            diff[i].append(diff[i-1][j+1] - diff[i-1][j])

        term = diff[i][0]
        for j in range(i):
            term *= (p - j) / (j + 1)
        result += term

    return result

x = list(map(float, input("Enter the values of x (space-separated): ").split()))
y = list(map(float, input("Enter the values of y (space-separated): ").split()))

value = float(input("Enter the intermediate value to be found: "))

interpolated_value = ForwardInterpolation(x, y, value)

if interpolated_value is not None:
    print("Interpolated value:", interpolated_value)