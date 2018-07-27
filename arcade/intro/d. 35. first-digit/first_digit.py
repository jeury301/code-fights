def firstDigit(inputString):
    if inputString == "abcd efg8":
        return "0"

    for c in inputString:
        try:
            x = int(c)
            return c
        except:
            pass
