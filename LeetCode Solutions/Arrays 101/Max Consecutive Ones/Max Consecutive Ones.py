class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOfOne = 0; 
        maximumCountOfOne = 0;
        for digit in nums:
            if (digit == 1):
                countOfOne += 1
                maximumCountOfOne = max(maximumCountOfOne, countOfOne)
            else:
                countOfOne = 0
        return maximumCountOfOne