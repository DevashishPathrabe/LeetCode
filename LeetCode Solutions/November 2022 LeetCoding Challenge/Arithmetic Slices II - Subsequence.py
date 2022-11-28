class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        result = 0
        for i in range(1, n):
            for j in range(i):
                difference = nums[i] - nums[j]
                count = 0
                if difference in dp[j]:
                    count = dp[j][difference]
                dp[i][difference] += count + 1
                result += count
        return result