class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) == 0):
            return [[]]
        sets = self.subsets(nums[1:])
        return sets + [[nums[0]] + s for s in sets]