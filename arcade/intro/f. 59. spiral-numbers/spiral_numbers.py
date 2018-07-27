def spiralNumbers(n):
    # building matrix
    m = build_matrix(n)
    # matrix corners
    corners = {(0, n-1), (n-1, n-1), (n-1, 0)}
    # to keep track of seen positions
    seen_pos = set()
    # initial values
    pos, num, dirr = (0, 0), 1, "right"

    while num <= n*n:
        m[pos[0]][pos[1]] = num
        num += 1
        seen_pos.add(pos)
        # updating position
        pos = update_pos(dirr)(pos[0], pos[1], n)
        # checking if updated pos is a corner
        if pos in corners:
            # if so, update direction
            dirr = update_dir(dirr)

        # checking if new pos is a wall
        if pos in seen_pos:
            pos = back_track(dirr)(pos[0], pos[1], n) # backtracking to pre pos
            dirr = update_dir(dirr) # updating direction
            pos = update_pos(dirr)(pos[0], pos[1], n) # updating position

    return m

def add(k, n):
    return (k+1) % (n-1) if (k + 1) % (n - 1) else (n - 1)

def sub(k, n):
    return (k-1) if (k-1) >= 0 else 0

def right(i, j, n):
    return i, add(j, n)

def down(i, j, n):
    return add(i, n), j

def left(i, j, n):
    return i, sub(j, n)

def up(i, j, n):
    return sub(i, n), j

def update_dir(dirr):
    # updatining a direction
    dir_map = {
        "right":"down",
        "down":"left",
        "left":"up",
        "up":"right"
    }
    return dir_map[dirr]

def update_pos(dirr):
    # updating position for given direction
    update_map = {
        "right":right,
        "down":down,
        "left":left,
        "up":up
    }
    return update_map[dirr]

def back_track(dirr):
    # backtracing a position for given direction
    back_map = {
        "right":left,
        "left":right,
        "down":up,
        "up":down
    }
    return back_map[dirr]

def build_matrix(n):
    # buiding n by n matrix
    return [[0 for j in range(n)] for i in range(n)]

    
