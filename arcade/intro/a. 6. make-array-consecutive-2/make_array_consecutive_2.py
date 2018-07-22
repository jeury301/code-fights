def makeArrayConsecutive2(statues):
    sorted_status = sorted(statues)

    missing = 0
    for i in range(sorted_status[0], sorted_status[-1]+1):
        if i not in statues:
            missing += 1

    return missing
