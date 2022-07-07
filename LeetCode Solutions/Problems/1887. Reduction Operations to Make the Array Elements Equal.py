class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        numberOfOperations, length = 0, len(count)-1
        for i in sorted(count.keys(), reverse=True):
            numberOfOperations += count[i]*length
            length -= 1
        return numberOfOperations