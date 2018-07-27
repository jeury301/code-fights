def findEmailDomain(address):
    tokens = address.split("@")
    return "" if len(tokens) < 2 else tokens[len(tokens)-1]
