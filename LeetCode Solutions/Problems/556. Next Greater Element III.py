class Solution:
    def nextGreaterElement(self, n: int) -> int:
        max_int = 2 ** 31 - 1
        digits = list(str(n))
        for i in range(len(digits)-2, -1, -1):
            for j in range(len(digits)-1, i, -1):
                if int(digits[i]) < int(digits[j]):
                    digits[i], digits[j] = digits[j], digits[i]
                    digits[i+1:] = list(sorted(digits[i+1:]))
                    res = int(''.join(digits))
                    return res if n < res <= max_int else -1
        return -1