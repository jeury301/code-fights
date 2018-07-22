from collections import Counter
def avoidObstacles(inputArray):
    k = sorted(inputArray[:])
    for i in range(1, max(k) + 2):
        j = Counter([x%i==0 for x in k])[False] == len(k)
        if j:
            return i
    return k[len(k) - i] + 1
