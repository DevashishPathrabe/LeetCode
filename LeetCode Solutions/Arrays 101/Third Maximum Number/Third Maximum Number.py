class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 1:
            return max(nums)
        if len(nums) == 2:
            return(max(nums))
        if len(nums) >= 3:
            return(nums[-3])