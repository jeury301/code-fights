def alternatingSums(a):
    return [sum([x for i, x in enumerate(a) if i % 2 == 0]),
            sum([x for i, x in enumerate(a) if i % 2 != 0])]
