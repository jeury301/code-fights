def addBorder(picture):
    rows, cols = len(picture), len(picture[0])
    final = ["*"*(cols+2)] * (rows + 2)

    for i, x in enumerate(picture):
        final[i+1] = "*" + x + "*"

    return final
    
