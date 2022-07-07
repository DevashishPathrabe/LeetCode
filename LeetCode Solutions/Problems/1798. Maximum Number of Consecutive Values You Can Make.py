class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins = sorted(coins)
        currentMax = 0
        for c in coins:
            if currentMax + 1 < c:
                break
            currentMax = currentMax + c
        return currentMax + 1