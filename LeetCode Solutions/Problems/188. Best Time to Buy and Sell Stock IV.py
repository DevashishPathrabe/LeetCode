class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) == 0:
            return 0
        minPrice, profit = [float('inf')] * k, [float('-inf')] * k
        for price in prices:
            minPrice[0] = min(minPrice[0], price)
            profit[0] = max(profit[0], price - minPrice[0])
            for i in range(1, k):
                minPrice[i] = min(minPrice[i], price - profit[i-1])
                profit[i] = max(profit[i], price - minPrice[i])
        return profit[k-1]