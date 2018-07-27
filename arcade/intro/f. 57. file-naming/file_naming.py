def fileNaming(names):
    seen = set()
    times = {}
    output = []
    for x in names:
        if x not in seen:
            output.append(x)
            seen.add(x)
            times[x] = 1
        else:
            to_add = x + "("+str(times[x])+")"
            times[x] += 1

            while to_add in seen:
                to_add = x + "("+str(times[x])+")"
                times[x] += 1
            output.append(to_add)
            seen.add(to_add)
            times[to_add] = 1
    return output
