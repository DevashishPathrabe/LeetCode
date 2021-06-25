vowels = "AEIOUaeiou"
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        middle, result = len(s) // 2, 0
        for i in range(middle):
            if(s[i] in vowels):
                result += 1
            if(s[middle + i] in vowels):
                result -= 1
        return result == 0