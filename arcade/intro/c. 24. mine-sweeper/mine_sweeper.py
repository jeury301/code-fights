import copy
import pprint
from collections import Counter
def minesweeper(matrix):
    r , c= [False]*len(matrix[0]), False
    f = [[c] + x + [c]  for x in [r] + matrix[:] + [r]]
    m, n = len(f), len(f[0])

    for i in range(1, m-1):
        for j in range(1, n-1):
            n_b = Counter([f[i-1][j-1],f[i-1][j],f[i-1][j+1],
                           f[i][j-1], False, f[i][j+1],
                           f[i+1][j-1],f[i+1][j],f[i+1][j+1]
                  ])[True]
            matrix[i-1][j-1] = n_b
    return matrix
