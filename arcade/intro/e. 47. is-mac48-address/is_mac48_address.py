import re
def isMAC48Address(inputString):
    groups = inputString.split("-")
    pttr = re.compile(r'^[0-9A-Fa-f][0-9A-Fa-f]$')

    if len(groups) != 6:
        return False

    return all([True if pttr.match(x) else False for x in groups])
