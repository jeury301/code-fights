from collections import Counter
def isBeautifulString(inputString):
    c, s = Counter(inputString), sorted(list(set(inputString)))
    prev = s[0]
    if prev != "a":
        return False
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(prev)) != 1:
            return False
        if c[s[i]] > c[prev]:
            return False
        prev = s[i]
    return True
