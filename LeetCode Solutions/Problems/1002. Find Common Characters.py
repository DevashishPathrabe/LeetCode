class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dp = [[]] * len(words)
        dp[0] = words[0]
        for i in range(1, len(words)):
            dp[i-1] = Counter(dp[i-1])
            chars = []
            for char in words[i]:
                if char in dp[i-1] and dp[i-1][char] > 0:
                    chars.append(char)
                    dp[i-1][char] -= 1
                dp[i] = chars
        return dp[-1]