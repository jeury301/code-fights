def validTime(time):
    tokens = time.split(":")
    hours, mins = tokens[0], tokens[1]

    if int(hours) < 0 or int(hours) > 23:
        return False
    if int(mins) < 0 or int(mins) > 59:
        return False

    return True
