class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring = ""
        for i in s:
            substring += i
            times = len(s) // len(substring)
            if times == 1:
                break
            if (substring*times) == s:
                return True
        return False