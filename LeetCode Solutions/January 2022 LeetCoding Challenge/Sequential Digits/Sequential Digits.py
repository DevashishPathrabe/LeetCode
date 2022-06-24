class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        nlow = len(str(low))
        nhigh = len(str(high))
        for i in range(nlow, nhigh + 1):
            for j in range(0, 10 - i):
                num = int(digits[j: j + i])
                if num >= low and num <= high:
                    result.append(num)
        return result