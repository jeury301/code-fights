def centuryFromYear(year):
    baseCentury = year / 100
    remainderCentury = 1 if year % 100 > 0 else 0

    return baseCentury + remainderCentury
