def absoluteValuesSumMinimization(a):
    min_x, x = sum([abs(y - a[0]) for y in a]), a[0]
    for i in range(1, len(a)):
        abs_x = sum([abs(y - a[i]) for y in a])
        if abs_x < min_x:
            min_x = abs_x
            x = a[i]
    return x
