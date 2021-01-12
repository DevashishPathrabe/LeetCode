class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def helper(s):
            if(s == ""):
                return True
            if(s in dp):
                return dp[s]
            for word in wordDict:
                if(word == s[:len(word)] and helper(s[len(word):])):
                    dp[s] = True
                    return True
                dp[s] = False
            return False
        return helper(s)