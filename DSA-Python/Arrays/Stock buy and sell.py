def stock(array):
    min_price=array[0]
    max_profit=0
    for i in array:
        if i<min_price:
            min_price=i
        if i-min_price>max_profit:
            max_profit=i-min_price
    return max_profit
o=[7,2,1,5,6,4,8]
print(o)
print(stock(o))