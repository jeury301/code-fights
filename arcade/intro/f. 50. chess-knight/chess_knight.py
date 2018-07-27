def chessKnight(cell):
    word_eb, cell = {chr(ord("a")+i):i for i in range(8)}, cell.lower()

    if (int(cell[1]) > 0 and
        int(cell[1]) <= 8 and
        word_eb.get(cell[0]) is not None):
        print(word_eb)
        print(cell)
        cell_moves = compute_moves(cell)
        print(cell_moves)
        normalized = [x
                      for x in cell_moves
                      if int(x[1]) > 0 and int(x[1]) <= 8 and word_eb.get(x[0]) is not None
                     ]
        print(normalized)
        return len(normalized)
    return 0

def compute_moves(cell):
    moves = []
    hor = chr(ord(cell[0])-2)+cell[1], chr(ord(cell[0])+2)+cell[1]
    ver = cell[0] + str(int(cell[1]) - 2), cell[0] + str(int(cell[1]) + 2)
    print(hor)
    print(ver)
    for m in hor:
        if (len(m) == 2 and
            m[1].isalnum and
            int(m[1])>0 and int(m[1]) <=8):
            l_m, r_m = m[0]+str(int(m[1])+1), m[0]+str(int(m[1])-1)
            if all([i.isalnum() for i in l_m]):moves.append(l_m)
            if all([i.isalnum() for i in r_m]):moves.append(r_m)

    for n in ver:
        if (len(n) == 2 and
            n[1].isalnum and
            int(n[1])>0 and int(n[1]) <=8):
            u_n, d_n = chr(ord(n[0])-1) + n[1], chr(ord(n[0])+1) + n[1]
            if all([i.isalnum() for i in u_n]):moves.append(u_n)
            if all([i.isalnum() for i in d_n]):moves.append(d_n)

    return moves
