class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]
        if(isPalindrome(s)):
            return True
        i, j = 0, len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                return isPalindrome(s[i:j]) or isPalindrome(s[i + 1:j + 1])
            i += 1
            j -= 1
        return False