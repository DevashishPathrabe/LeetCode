class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        result = count1 = count2 = 0
        for c in text:
            if c == pattern[1]:
                result += count1
                count2 += 1
            if c == pattern[0]:
                count1 += 1
        return result + max(count1, count2)