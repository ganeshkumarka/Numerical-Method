def gauss_jordan(matrix):
    n = len(matrix)                                                            

    for i in range(n):
        pivot = matrix[i][i]                                                   

        for j in range(i, n + 1):
            matrix[i][j] /= pivot                                              

        for j in range(n):
            if j != i:                                                         
                eq = matrix[j][i]                                             
                for k in range(i, n + 1):                                       
                    matrix[j][k] -= eq * matrix[i][k]

matrix = [[2, 2, 1, 6],
          [4, 2, 3, 4],
          [1, 1, 1, 0]]

gauss_jordan(matrix)

for i in range(len(matrix)):
    print("x", i + 1, "=", matrix[i][-1])