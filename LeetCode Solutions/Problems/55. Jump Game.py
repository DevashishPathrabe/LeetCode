class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 1   
        for i in range(len(nums)-2, -1, -1):
            if(nums[i] >= jump):
                jump = 1
            else:
                jump += 1
        if(len(nums) > 1):
            return nums[0] >= jump
        else:
            return True