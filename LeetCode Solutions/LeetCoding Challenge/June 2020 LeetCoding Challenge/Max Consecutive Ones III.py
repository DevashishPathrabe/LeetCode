class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maximumNumberOfConsecutive, left, count = 0, 0, 0
        for i in range(len(nums)):
            if not nums[i]:
                count += 1
                while left <= i and count > k:
                    if nums[left] == 0:
                        count -= 1
                    left += 1
            maximumNumberOfConsecutive = max(maximumNumberOfConsecutive, i-left+1)
        return maximumNumberOfConsecutive