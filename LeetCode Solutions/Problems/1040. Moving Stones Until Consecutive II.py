class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        high = max(stones[-1] - stones[1], stones[-2] - stones[0]) - (len(stones) - 2)
        a, low = 0, inf
        for i in range(len(stones)): 
            while stones[i] - stones[a] >= len(stones):
                a += 1
            if i - a + 1 == stones[i] - stones[a] + 1 == len(stones) - 1:
                low = min(low, 2)
            else:
                low = min(low, len(stones) - (i - a + 1))
        return [low, high]