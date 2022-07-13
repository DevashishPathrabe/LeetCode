class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if(nums[j] != 0):
                nums[i] = nums[j]
                if(j != i):
                    nums[j] = 0
                i += 1