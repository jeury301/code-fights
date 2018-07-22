def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True
    prev = None
    for i, x in enumerate(sequence):
        if prev > x:
            for m in range(2):
                test = [p for j, p in enumerate(sequence) if j != (i - m)]
                if test == sorted(test) and len(test) == len(set(test)):
                        return True
        prev = x
    return False
