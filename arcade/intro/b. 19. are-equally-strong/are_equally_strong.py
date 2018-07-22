def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    m, f = [yourLeft, yourRight], [friendsLeft, friendsRight]
    return (max(m) == max(f)) and (sum(m) == sum(f))
