class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        return sum(count[n]*count[n+k] for n in count.keys())  