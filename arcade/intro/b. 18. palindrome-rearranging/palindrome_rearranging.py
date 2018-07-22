from collections import Counter
def palindromeRearranging(inputString):
    c = Counter(inputString)
    n = 0
    for k in c:
        if c[k] % 2 != 0:
            n += 1
    return n <= 1
