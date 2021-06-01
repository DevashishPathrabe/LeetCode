class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return 0
        nums.sort()
        maximumDifference = 0
        for num in range(1, len(nums)):
            maximumDifference = max(maximumDifference, nums[num]-nums[num - 1])
        return maximumDifference