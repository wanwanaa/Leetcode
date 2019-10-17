# 122.买卖股票的最佳时期II
# 1. 手里有股票（买入）
# 2. 手里没有股票（卖出）
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp_0 = 0
    dp_1 = -sys.maxint
    for i in range(len(prices)):
        temp = dp_0
        dp_0 = max(dp_0, dp_1 + prices[i])
        dp_1 = max(dp_1, temp - prices[i])
    return dp_0