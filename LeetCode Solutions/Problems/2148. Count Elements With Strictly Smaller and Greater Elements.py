class Solution:
    def countElements(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] > minimum and nums[i] < maximum:
                count += 1
        return count