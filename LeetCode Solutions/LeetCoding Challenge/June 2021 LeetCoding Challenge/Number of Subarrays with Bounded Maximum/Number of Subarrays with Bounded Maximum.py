class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        numberOfSubarrays, lower, middle = 0, 0, 0
        for num in nums:
            if (num > right):
                middle = 0
            else:
                middle += 1
                numberOfSubarrays += middle
            if (num >= left):
                lower = 0
            else:
                lower += 1
                numberOfSubarrays -= lower
        return numberOfSubarrays