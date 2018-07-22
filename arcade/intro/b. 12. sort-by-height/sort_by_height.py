def sortByHeight(a):
    trees = {}
    not_trees = []

    for i, x in enumerate(a):
        if x == -1:
            trees[i] = -1
        else:
            not_trees.append(x)
    not_trees = sorted(not_trees)

    final = []
    index = 0
    for i in range(len(a)):
        if trees.get(i):
            final.append(trees.get(i))
        else:
            final.append(not_trees[index])
            index += 1
    return final
