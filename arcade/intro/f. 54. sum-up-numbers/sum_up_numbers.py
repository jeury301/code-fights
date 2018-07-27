def sumUpNumbers(inputString):
    numbers = []
    curr = ""

    for i in inputString:
        try:
            x = int(i)
            curr += i
        except:
            if curr != "":
                numbers.append(curr)
                curr = ""
    if curr != "":
        numbers.append(curr)

    return sum([int(x) for x in numbers])
