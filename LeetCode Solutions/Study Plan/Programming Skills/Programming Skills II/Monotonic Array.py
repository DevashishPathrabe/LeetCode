class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = False
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                increasing = True
            if nums[i+1] < nums[i]:
                decreasing = True
            if increasing == decreasing == True:
                return False
        return True