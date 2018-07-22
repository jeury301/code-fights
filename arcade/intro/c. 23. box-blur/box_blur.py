import copy
def boxBlur(image):
    k, i_k, f= [copy.deepcopy(r) for r in image], [-1, 0, 1], [copy.deepcopy(r) for r in image]
    m, n = len(k), len(k[0])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            n_b = [sum([k[i+x][j+y] for y in i_k]) for x in i_k]
            print(n_b)
            f[i][j] = int(sum(n_b)/9)
    f = f[1:m-1]
    f = [r[1:n-1] for r in f]
    return f
