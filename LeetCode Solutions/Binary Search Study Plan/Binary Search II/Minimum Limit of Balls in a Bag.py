class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def helper(target):
            if target == 0:
                return maxOperations + 1
            count = 0
            for num in nums:
                count += (num - 1) // target
            return count <= maxOperations
        left, right = max(sum(nums) // (len(nums) + maxOperations), 1), max(nums)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left