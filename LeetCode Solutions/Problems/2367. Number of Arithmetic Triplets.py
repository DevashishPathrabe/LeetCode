class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        items = set(nums)
        results = 0
        for i in nums:
            j = i + diff
            k = j + diff
            if j in items and k in items:
                results += 1
        return results