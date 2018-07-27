def stringsRearrangement(old, new = []):
    if old:
        for option in old:
            clone = old[:]
            clone.remove(option)
            result = stringsRearrangement(clone, new + [option])
            if result:
                return result
        return False
    return filter(new)


def filter(current):
    if current:
        first = current[0]
        for i in range(1, len(current)):
            added = sum([1 if first[j]==current[i][j] else 0 for j in range(len(current[i]))])
            if added != len(current[i]) -1:
                return False
            first = current[i]
    return True
        
