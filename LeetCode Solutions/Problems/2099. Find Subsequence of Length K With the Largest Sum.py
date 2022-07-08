class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr, maximumK = [], sorted(nums, reverse=True)[:k]
        for num in nums:
            if num in maximumK:
                arr.append(num)
                maximumK.remove(num)
                if len(maximumK) == 0:
                    return arr