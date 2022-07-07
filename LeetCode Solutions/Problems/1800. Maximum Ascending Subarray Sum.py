class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += nums[i]
            else:
                result = max(result, current)
                current = nums[i]
        return max(result, current)