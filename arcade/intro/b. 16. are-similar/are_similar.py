from collections import Counter
def areSimilar(a, b):
    return Counter(a) == Counter(b) and sum([1 for x, y in zip(a, b) if x != y]) < 3
