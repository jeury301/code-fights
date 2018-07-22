from collections import Counter

def commonCharacterCount(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    return sum([min([c1[x], c2[x]]) for x in list(set(s1) and set(s2))])
