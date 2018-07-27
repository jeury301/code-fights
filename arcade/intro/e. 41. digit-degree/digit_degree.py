def digitDegree(n):
    degree = 0
    while(n > 9):
        n = sum([int(i) for i in str(n)])
        degree += 1

    return degree
