def maxProfit(prices) :
    min_price=prices[0]
    max_profit=0


    for price in prices[1:]:
      min_price = min(min_price, price)
      max_profit=max(max_profit,price-min_price)

    return max_profit

print(maxProfit([1,2,3,5,6,10]))