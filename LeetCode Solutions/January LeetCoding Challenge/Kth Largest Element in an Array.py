class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if(not nums or not k or k < 0):
            return None
        visited, n, largestElement = set(), len(nums), None
        for i in range(k):
            maxIndex, maxValue = -1, -sys.maxsize
            for i, value in enumerate(nums):
                if(i in visited):
                    continue
                if(value > maxValue):
                    maxIndex, maxValue = i, value
            largestElement = maxValue
            visited.add(maxIndex)
        return largestElement