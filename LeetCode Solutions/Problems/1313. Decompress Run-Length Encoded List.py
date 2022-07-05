class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i, n, decompressedList = 0, len(nums), []
        if n == 1:
            return nums
        while (i < n-1):
            for _ in range(0,nums[i]):
                decompressedList.append(nums[i+1])
            i += 2
        return decompressedList