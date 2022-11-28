class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        numberOfOperations, sum, i, j = 0, 0, 0, len(nums)-1
        while (i < j):
            sum = nums[i] + nums[j]
            if (sum == k):
                i += 1
                j -= 1
                numberOfOperations += 1
            elif (sum < k):
                i += 1
            else:
                j -= 1
        return numberOfOperations