class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        palindrome = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            palindrome[i][i] = 1
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    palindrome[i][j] = palindrome[i + 1][j - 1] + 2
                else:
                    palindrome[i][j] = max(palindrome[i + 1][j], palindrome[i][j - 1])
        return palindrome[0][-1]