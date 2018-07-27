from collections import Counter
def electionsWinners(votes, k):
    max_v = max(votes)
    total_v = Counter(votes)[max_v]

    if k == 0:
        if total_v == 1: return 1
        return 0

    return sum([1 if x+k > max_v else 0 for x in votes])
