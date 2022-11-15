class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = []
        for index, i in enumerate(number):
            if i == digit:
                result.append(int(number[:index]+number[index+1:]))
        return str(max(result))