class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i, j, n = nums.index(min(nums)), nums.index(max(nums)), len(nums)
        return min(max(i + 1, j + 1), max(n - i, n - j), i + 1 + n - j, j + 1 + n - i)