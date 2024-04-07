def gauss(matrix):
    n = len(matrix)                                                           

    for i in range(n):
        pivot = matrix[i][i]                                                  

        for j in range(n):
            if j != i:                                                         
                eq = matrix[j][i] / pivot                                       
                for k in range(n + 1):                                      
                    matrix[j][k] -= eq * matrix[i][k]

        pivot = matrix[i][i]                                                    
        for j in range(n + 1):
            matrix[i][j] /= pivot

    solutions = [0] * n
    for i in range(n - 1, -1, -1):
        solutions[i] = matrix[i][n]
        for j in range(i + 1, n):
            solutions[i] -= matrix[i][j] * solutions[j]

    return solutions

matrix = [[2, 2, 1, 6],
          [4, 2, 3, 4],
          [1, 1, 1, 0]]

solutions = gauss(matrix)

for i, solution in enumerate(solutions):
    print("x", i + 1, "=", solution)