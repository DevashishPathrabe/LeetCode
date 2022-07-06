class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def helper(Bottles: int, total: int):
            exchanged = Bottles // numExchange
            rest = Bottles % numExchange
            if(exchanged == 0):
                return total
            total += exchanged
            return helper(exchanged+rest, total)
        return helper(numBottles, numBottles)