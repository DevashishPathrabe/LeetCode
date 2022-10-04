class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums) - 1):
            getSum = nums[i] + nums[i + 1]
            if getSum in sums:
                return True
            sums.add(getSum)
        return False