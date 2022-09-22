class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        max_length = 0
        for i in s:
            if i in result:
                result = result[result.index(i)+1:]+i
            else:
                result += i
            max_length = max(max_length, len(result))
        return (max_length)