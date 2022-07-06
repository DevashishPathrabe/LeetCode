class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        minDifference = nums[-1] - nums[0]
        minDifference = min(nums[-1] - nums[3], nums[-4] - nums[0])
        minDifference = min(nums[-2] - nums[2], minDifference)
        minDifference = min(nums[-3] - nums[1], minDifference)
        return minDifference