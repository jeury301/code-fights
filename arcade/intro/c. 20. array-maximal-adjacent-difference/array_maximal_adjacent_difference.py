def arrayMaximalAdjacentDifference(inputArray):
    k = inputArray[:]
    return max([abs(k[i]-k[i - 1]) for i in range(1, len(k))])
