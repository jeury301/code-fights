def knapsackLight(value1, weight1, value2, weight2, maxW):
    w, v = [weight1, weight2], [value1, value2]
    k_w, k_v= ({weight1:value1, weight2:value2},
               {value1:weight1, value2:weight2})
    if sum(w) <= maxW:
        return sum(v)
    if k_v.get(max(v)) <= maxW:
        return max(v)
    if k_w.get(maxW):
        return k_w.get(maxW)
    if min(w) > maxW:
        return 0
