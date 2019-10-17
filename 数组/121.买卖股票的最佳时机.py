# 121.买卖股票的最佳时机
# 1. 寻找当前最小值
# 2. 卖出得到收益
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minprice = sys.maxint
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        else:
            profit = prices[i] - minprice
            if profit > maxprofit:
                maxprofit = profit
    return maxprofit