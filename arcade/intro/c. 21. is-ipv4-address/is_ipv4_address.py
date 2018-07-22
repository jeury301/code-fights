from collections import Counter
def isIPv4Address(inputString):
    try:
        k = Counter([int(x) <= 255 for x in inputString.split(".")])
        return k[True] == 4
    except:
        return False
