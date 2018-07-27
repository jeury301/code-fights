from collections import Counter
def differentSymbolsNaive(s):
    return len(dict(Counter(s)).keys())
