class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        dp = [0]*(len(prices)+1)
        for i in range(len(prices)):
            curr_min = min(curr_min ,prices[i])
            dp[i+1] = max(prices[i]-curr_min, dp[i])
        maximumProfit = max(dp[-1], 0)
        curr_max = 0
        for j in range(len(prices)-1,0,-1):
            curr_max = max(curr_max, prices[j])
            maximumProfit = max(maximumProfit, dp[j] + curr_max - prices[j])
        return maximumProfit