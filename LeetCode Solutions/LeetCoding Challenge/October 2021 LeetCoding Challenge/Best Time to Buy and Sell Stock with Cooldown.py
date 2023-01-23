class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n <= 1):
            return 0
        stock = [0] * n
        cash = [0] * n
        stock[0] = -1 * prices[0]
        stock[1] = max(stock[0], -1 * prices[1])
        cash[1] = max(0, stock[0] + prices[1])
        for i in range(2, n):
            stock[i] = max(stock[i-1], cash[i-2] - prices[i])
            cash[i] = max(cash[i-1], stock[i-1] + prices[i])
        return cash[n-1]