def adjacentElementsProduct(inputArray):
    first, second = 0, 1
    lp = inputArray[first]*inputArray[second]

    for index in range(2, len(inputArray)):
        first = second
        second = index
        new_lp = inputArray[first]*inputArray[second]

        if new_lp > lp:
            lp = new_lp

    return lp

    
