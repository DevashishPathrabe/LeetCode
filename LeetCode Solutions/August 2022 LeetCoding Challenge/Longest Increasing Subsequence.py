class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        List = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i] > nums[j]):
                    if(List[i] <= List[j]):
                        List[i] = List[j]+1 
        return max(List)