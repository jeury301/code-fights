def messageFromBinaryCode(code):
    letters, binaries = [], []
    letter = ""
    for i, x in enumerate(code):
        letter += x
        if len(letter) == 8:
            binaries.append(letter)
            letters.append(chr(bin2dec(letter)))
            letter = ""

    if letter != "":
        binaries.append(letter)
        letters.append(bin2dec(letter))

    return "".join(letters)

def bin2dec(bin):
    final = 0
    print(bin)
    for i, x in enumerate(bin[::-1]):
        if int(x) != 0:
            final += 2**i
    return final
