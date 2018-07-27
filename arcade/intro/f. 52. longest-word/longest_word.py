def longestWord(text):
    tokens = "".join([i if i.isalnum() else " " for i in text]).split(" ")
    clean_tokens = ["".join([i for i in x if i.isalnum()]) for x in tokens]
    return sorted(clean_tokens, key=len)[::-1][0]
