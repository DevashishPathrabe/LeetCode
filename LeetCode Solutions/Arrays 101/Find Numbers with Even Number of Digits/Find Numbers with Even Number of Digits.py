class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for digit in nums:
            numberOfDigits = 0
            while (digit > 0):
                digit = digit // 10
                numberOfDigits += 1
            if (numberOfDigits % 2 == 0):
                count += 1
        return count
        