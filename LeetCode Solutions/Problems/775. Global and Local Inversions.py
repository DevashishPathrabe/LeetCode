class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if(i-nums[i] > 1 or i-nums[i] < -1):
                return False
        return True