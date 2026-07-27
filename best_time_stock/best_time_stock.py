def best_time_stock(prices):
    if(len(prices) == 0):
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if(prices[i] < min_price):
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            if(profit > max_profit):
                max_profit = profit
    return max_profit

prices = [7,1,5,3,6,4]
print("The Max Profit is :", best_time_stock(prices))
            