class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True
        dp = nums[:]
        for i in range(1, n):
            for j in range(n - i):
                dp[j] = max(nums[j] - dp[j + 1], nums[j + i] - dp[j])
        return dp[0] >= 0