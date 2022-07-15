class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for i in range(len(nums)):
            if (nums[i] > first):
                second = min(second, nums[i])
            if (nums[i] > second):
                return True
            first = min(first, nums[i])
        return False