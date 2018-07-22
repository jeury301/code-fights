def depositProfit(deposit, rate, threshold):
    d, y = deposit, 0
    while(d < threshold):
        d, y= d + (d*rate)/100, y+1
        print(rate, d, y)
    return y
 
