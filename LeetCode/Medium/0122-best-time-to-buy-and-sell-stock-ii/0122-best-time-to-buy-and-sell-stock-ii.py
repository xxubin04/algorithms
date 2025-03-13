class Solution(object):
    def maxProfit(self, prices):
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = dp[i-1]
            if prices[i] > prices[i-1]:
                dp[i] += prices[i] - prices[i-1]

        return dp[-1]