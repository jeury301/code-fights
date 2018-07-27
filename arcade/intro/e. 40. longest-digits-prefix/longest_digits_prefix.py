def longestDigitsPrefix(inputString):
    pre = ""
    for i in inputString:
        try:
            x = int(i)
            pre += i
        except:
            break
    return pre
