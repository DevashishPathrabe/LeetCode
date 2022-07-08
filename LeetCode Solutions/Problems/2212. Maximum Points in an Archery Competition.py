class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        @lru_cache(None)
        def dp(k, numArrows):
            if k == 12 or numArrows <= 0:
                return 0
            maxScore = dp(k+1, numArrows)
            if numArrows > aliceArrows[k]:
                maxScore = max(maxScore, dp(k+1, numArrows-aliceArrows[k]-1) + k)
            return maxScore
        ans = [0] * 12
        remainBobArrows = numArrows
        for k in range(12):
            if dp(k, numArrows) != dp(k+1, numArrows):
                ans[k] = aliceArrows[k] + 1
                numArrows -= ans[k]
                remainBobArrows -= ans[k]
        ans[0] += remainBobArrows
        return ans