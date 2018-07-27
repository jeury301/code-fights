def growingPlant(upSpeed, downSpeed, desiredHeight):
    current = 0
    days = 1
    while(current < desiredHeight):
        current += upSpeed
        if current >= desiredHeight:
            break
        current -= downSpeed
        if current >= desiredHeight:
            break
        days += 1
    return days
