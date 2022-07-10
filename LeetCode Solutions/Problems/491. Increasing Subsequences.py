class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(current, nums):
            if (len(current) >= 2 and current[-1] < current[-2]):
                return
            if (len(current) >= 2 and current[:] not in result):
                result.add(current[:])
            for i in range(len(nums)):
                helper(current + (nums[i],), nums[i+1:] )
        result = set()
        helper((), nums)
        return result