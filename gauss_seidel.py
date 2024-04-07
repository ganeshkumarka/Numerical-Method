def gauss_seidel(matrix, initial_guess, tolerance=0.00001, max_iterations=100):
    n = len(matrix)
    x = initial_guess[:]
    x_new = [0] * n

    for _ in range(max_iterations):
        max_error = 0.0
        for i in range(n):
            sum_ = sum(matrix[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (matrix[i][n] - sum_) / matrix[i][i]
            error = abs(x_new[i] - x[i])
            if error > max_error:
                max_error = error

        if max_error < tolerance:
            return x_new

        x = x_new[:]

    raise ValueError("Gauss-Seidel method did not converge within the specified number of iterations.")

matrix = [[3, -0.1, -0.2, 7.85],
          [0.1, 7, -0.3, -19.3],
          [0.3, -0.2, 10, 71.4]]

initial_guess = [0, 0, 0]

solution = gauss_seidel(matrix, initial_guess)
print("Solution:", solution)