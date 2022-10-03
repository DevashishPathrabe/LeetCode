class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[-1]
        dp = [0] * (n + 1)
        for i in nums:
            dp[i] += i
        dp1 = 0
        dp2 = 0
        for i in range(n+1):
            temp = max(dp2, dp1 + dp[i])
            dp1 = dp2
            dp2 = temp
        return temp