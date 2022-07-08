class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            maximum = nums[i]
            minimum = nums[i]
            for j in range(i+1, n):
                if nums[j] > maximum:
                    maximum = nums[j]
                elif nums[j] < minimum:
                    minimum = nums[j]
                result += (maximum - minimum)
        return result