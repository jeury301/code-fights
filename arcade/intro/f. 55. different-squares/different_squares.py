import numpy as np

def differentSquares(k):
    rows, cols = len(k), len(k[0])
    seen = set()

    for i in range(rows):
        for j in range(cols):
            if i > 0 and j > 0:
                temp = "".join([str(k[i-1][j-1]), str(k[i-1][j]),
                                str(k[i][j-1]), str(k[i][j])])
                if temp not in seen:
                    seen.add(temp)
    return len(seen)





    
