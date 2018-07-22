def allLongestStrings(inputArray):
    longest = max([len(x) for x in inputArray])
    return [y for y in inputArray if len(y) == longest]
