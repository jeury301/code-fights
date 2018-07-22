def chessBoardCellColor(cell1, cell2):
    board = {
        chr(ord("a")+i):[0 if j%2==0 else 1 for j in range(1, 9)]
        if i%2 == 0
        else
        [1 if j%2==0 else 0 for j in range(1, 9)]
        for i in range(8)
    }
    c1, c2 = [i for i in cell1.lower()], [i for i in cell2.lower()]

    return board[c1[0]][int(c1[1])-1] == board[c2[0]][int(c2[1])-1]
