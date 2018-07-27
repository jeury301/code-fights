def buildPalindrome(st):
    k = [i for i in st]
    to_append = []
    while(checkPalin(k) is False):
        to_append.append(k[0])
        k = k[1:]
    to_append = "".join(to_append[::-1])
    return st + to_append

def checkPalin(t):
    for i in range(len(t)):
        if t[i] != t[len(t) - (i + 1)]:
            return False
    return True
        
