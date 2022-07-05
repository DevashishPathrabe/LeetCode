class Solution:
    def reformat(self, s: str) -> str:
        numbers = [c for c in s if c.isdigit()]
        letters = [c for c in s if c.isalpha()]
        if abs(len(numbers) - len(letters)) > 1:
            return ""
        result, i = "", 0
        if len(letters) > len(numbers):
            result += letters[-1]
        while i < len(numbers) and i < len(letters):
            result += numbers[i]
            result += letters[i]
            i += 1
        if len(numbers) > len(letters):
            result += numbers[-1]
        return result