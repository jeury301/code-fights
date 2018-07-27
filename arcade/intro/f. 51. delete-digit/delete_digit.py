def deleteDigit(n):
    all_perms = []
    i_input = [i for i in str(n)]

    for i in i_input:
        clone = i_input[:]
        clone.remove(i)
        all_perms.append(clone)

    print(all_perms)
    max_n = max([int(''.join(x)) for x in all_perms if int(''.join(x)) <= n])
    return max_n
