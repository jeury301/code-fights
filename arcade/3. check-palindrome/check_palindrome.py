def checkPalindrome(inputString):
    lower = 0
    upper = len(inputString) - 1

    middle = (len(inputString)/2 - 1) if len(inputString) % 2 == 0 else ((len(inputString) - 1)/2 )

    print lower
    print upper
    print middle

    is_poly = True
    while(lower <= middle):
        if inputString[lower] != inputString[upper]:
            is_poly = False
            break
        lower += 1
        upper -= 1

    return is_poly

            
