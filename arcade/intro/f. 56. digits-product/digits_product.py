import operator
import functools
def digitsProduct(product):
    if product == 0:
        return 10
    for x in range(product*10):
        made_up_p = functools.reduce(operator.mul,
                             [int(i) for i in str(x)], 1)
        if made_up_p == product:
            return x
    return -1
