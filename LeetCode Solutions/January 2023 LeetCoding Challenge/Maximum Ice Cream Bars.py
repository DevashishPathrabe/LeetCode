class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:
                return i
        return len(costs)