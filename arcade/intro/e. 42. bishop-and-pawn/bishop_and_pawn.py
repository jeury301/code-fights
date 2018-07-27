def bishopAndPawn(bishop, pawn):
    trans = {chr(ord("a")+i):i for i in range(8)}
    b_pos, p_pos = (trans[bishop[0]]*8 + int(bishop[1]),
                    trans[pawn[0]]*8 + int(pawn[1]))
    print(b_pos, p_pos)
    if p_pos > b_pos:
        b_pos = b_pos+8*abs(int(pawn[1])-int(bishop[1]))+int(pawn[1])-int(bishop[1])
    else:
        b_pos = b_pos-8*abs(int(pawn[1])-int(bishop[1]))+int(pawn[1])-int(bishop[1])

    return b_pos == p_pos
