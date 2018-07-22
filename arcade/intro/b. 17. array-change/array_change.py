def arrayChange(inputArray):
    k , steps = inputArray[:], 0
    for i in range(1, len(k)):
        curr = k[i]
        if curr <= k[i - 1]:
            v = (k[i - 1] - curr) + 1
            curr, steps = curr + v, steps + v
        k[i] = curr
    return steps
        
