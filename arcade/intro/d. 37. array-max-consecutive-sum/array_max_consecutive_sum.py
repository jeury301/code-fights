def arrayMaxConsecutiveSum(inputArray, k):
    curr_sum = max_sum = sum([inputArray[i] for i in range(k)])

    for i in range(k, len(inputArray)):
        curr_sum = curr_sum + inputArray[i] - inputArray[i - k]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum
