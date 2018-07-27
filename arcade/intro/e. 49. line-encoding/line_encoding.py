from collections import Counter
def lineEncoding(s):
    curr, count, f = s[0], 1, ""

    for i in range(1, len(s)):
        if s[i] != curr:
            if count != 1:
                f += str(count)
            f += curr
            count, curr = 1, s[i]
        else:
            count += 1
    if count != 1:
        f += str(count)
    f += curr
    return f
