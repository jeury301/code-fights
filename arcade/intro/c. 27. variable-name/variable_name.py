import re
def variableName(name):
    to_m = re.compile(r"^[A-Za-z_][a-zA-Z0-9_]*")
    return bool(to_m.fullmatch(name))
