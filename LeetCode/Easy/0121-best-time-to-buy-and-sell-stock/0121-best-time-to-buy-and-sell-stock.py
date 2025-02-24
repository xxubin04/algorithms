class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                max_profit = max(max_profit, prices[sell]-prices[buy])

        return max_profit