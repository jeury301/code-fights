def isLucky(n):
    return (True if
           sum([int(x) for x in str(n)[:len(str(n))/2]]) ==
           sum([int(x) for x in str(n)[len(str(n))/2:]]) else
            False
           )
