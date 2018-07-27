def sudoku(grid):
    n = 3
    # checking subgrids
    is_subgrids = check_subgrids(grid, n)
    # check horizontals
    is_horizontals = check_horizontals(grid, n*3)
    # check verticals
    is_verticals = check_verticals(grid, n*3)

    return is_subgrids and is_horizontals and is_verticals

def check_subgrids(grid, n):
    for i_grid in range(n):
        for j_grid in range(n):
            seen_nums = set()
            for i in range(n):
                for j in range(n):
                    if grid[i + 3*i_grid][j + 3*j_grid] in seen_nums:
                        return False
                    seen_nums.add(grid[i + 3*i_grid][j + 3*j_grid])
            if sum([x for x in seen_nums]) != 45:
                return False
    return True

def check_horizontals(grid, n):
    for i in range(n):
        seen_nums = set()
        for j in range(n):
            if grid[i][j] in seen_nums:
                return False
            seen_nums.add(grid[i][j])
        if sum([x for x in seen_nums]) != 45:
            return False
    return True

def check_verticals(grid, n):
    for i in range(n):
        seen_nums = set()
        for j in range(n):
            if grid[j][i] in seen_nums:
                return False
            seen_nums.add(grid[j][i])
        if sum([x for x in seen_nums]) != 45:
            return False
    return True
