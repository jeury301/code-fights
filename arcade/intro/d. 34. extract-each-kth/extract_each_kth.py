def extractEachKth(inputArray, k):
    return [x for i, x in enumerate(inputArray) if (i+1)%k != 0]
