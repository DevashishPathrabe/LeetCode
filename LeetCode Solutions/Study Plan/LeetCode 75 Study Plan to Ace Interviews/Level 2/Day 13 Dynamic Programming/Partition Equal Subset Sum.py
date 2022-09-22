class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2:
            return False
        dp = dict()
        def backtrack(index, local):
            if index >= n:
                return False
            if total - local == local:
                return True
            if (index, local) in dp:
                return dp[(index, local)]
            dp[(index, local)] = backtrack(index + 1, local + nums[index]) or backtrack(index + 1, local)
            return dp[(index, local)]
        return backtrack(0, 0)