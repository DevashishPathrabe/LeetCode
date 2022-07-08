class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, val = 0, 1
        for i in range(len(prices)-1):
            if prices[i] == prices[i+1]+1:
                val += 1
            else:
                ans += (val*(val+1)) // 2
                val = 1
        return ans + (val*(val+1)) // 2