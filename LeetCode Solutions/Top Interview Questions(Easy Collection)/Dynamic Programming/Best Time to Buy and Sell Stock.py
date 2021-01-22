class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(not prices):
            return 0
        buyingPrice = sys.maxsize
        maximumProfit = 0
        for i, j in enumerate(prices):
            if(j < buyingPrice):
                buyingPrice = j
            profit = prices[i] - buyingPrice
            if(profit > maximumProfit):
                maximumProfit = profit
        return maximumProfit