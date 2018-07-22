def matrixElementsSum(matrix):
    suited = 0
    zeros = []
    for row in matrix:
        for i, col in enumerate(row):
            if col != 0 and i not in zeros:
                suited += col
            else:
                zeros.append(i)
    return suited
