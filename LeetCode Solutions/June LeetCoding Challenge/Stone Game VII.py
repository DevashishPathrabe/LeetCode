class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dpCurrent, dpLast = [0]*len(stones), [0]*len(stones)
        for i in range(len(stones)-2, -1, -1):
            total = stones[i]
            dpLast, dpCurrent = dpCurrent, dpLast
            for j in range(i+1, len(stones)):
                total += stones[j]
                dpCurrent[j] = max(total - stones[i] - dpLast[j], total - stones[j] - dpCurrent[j-1])
        return dpCurrent[-1]