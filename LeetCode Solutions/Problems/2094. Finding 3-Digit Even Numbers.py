class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        arr, digits = [], Counter(digits)
        for i in range(100, 1000, 2):
            digitCount = Counter(map(int, str(i)))
            for digit, count in digitCount.items():
                if count > digits[digit]:
                    break
            else:
                arr.append(i)
        return arr