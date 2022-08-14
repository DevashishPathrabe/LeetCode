class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        mx = float('inf')
        N = len(nums)
        currentSum = 0
        for right in range(N):
            currentSum += nums[right]
            while currentSum >= target:
                mx = min(mx, right - left + 1)
                currentSum -= nums[left]
                left += 1
        return 0 if mx == float('inf') else mx