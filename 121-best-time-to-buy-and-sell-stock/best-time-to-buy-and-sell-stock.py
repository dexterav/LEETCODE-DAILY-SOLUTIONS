class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0

        for price in prices:
            if price<buy:
                buy=price

            currentProfit = price-buy

            if currentProfit>profit:
                profit=currentProfit

        return profit                 