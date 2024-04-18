# def gauss(matrix):
#     n = len(matrix)                                                           

#     for i in range(n):
#         pivot = matrix[i][i]                                                  

#         for j in range(n):
#             if j != i:                                                         
#                 eq = matrix[j][i] / pivot                                       
#                 for k in range(n + 1):                                      
#                     matrix[j][k] -= eq * matrix[i][k]

#         pivot = matrix[i][i]                                                    
#         for j in range(n + 1):
#             matrix[i][j] /= pivot

#     solutions = [0] * n
#     for i in range(n - 1, -1, -1):
#         solutions[i] = matrix[i][n]
#         for j in range(i + 1, n):
#             solutions[i] -= matrix[i][j] * solutions[j]

#     return solutions

# matrix = [[2, 2, 1, 6],
#           [4, 2, 3, 4],
#           [1, 1, 1, 0]]

# solutions = gauss(matrix)

# for i, solution in enumerate(solutions):
#     print("x", i + 1, "=", solution)
import numpy as np
import sys

n = int(input('Enter number of unknowns: '))
a = np.zeros((n,n+1))
x = np.zeros(n)

print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]

        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]

    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]

    x[i] = x[i]/a[i][i]

print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')