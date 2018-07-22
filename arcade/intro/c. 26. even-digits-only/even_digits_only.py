def evenDigitsOnly(n):
    print(n)
    n, even = help(n)
    if not even: return even
    while n >= 1:
        print(n)
        n, even = help(n)
        if not even: return even
    return True

def help(n):
    r, n = int(n%10), int(n/10)
    if r % 2 != 0:
        return int(n), False
    return n, True
