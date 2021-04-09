class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) < 2):
            return s
        dp, palindromeSubstring = [[0]*len(s) for i in range(len(s))], {}
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if(s[i] == s[j] and ((j - i + 1) <= 3 or dp[i + 1][j - 1])):
                    dp[i][j] = True
                    palindromeSubstring[j-i+1] = s[i:j+1]
                else:
                    dp[i][j] = False
        return palindromeSubstring[max(palindromeSubstring)]