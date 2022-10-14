class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1 = 0
        count2 = 0
        for i in nums:
            if(i == 1):
                count1 += 1
            if(i == 2):
                count2 += 1
        for i in range(len(nums) - count1 - count2):
            nums[i] = 0
        for i in range(len(nums) - count1 - count2, len(nums) - count2):
            nums[i] = 1
        for i in range(len(nums) - count2, len(nums)):
            nums[i] = 2