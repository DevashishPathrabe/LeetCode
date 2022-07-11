class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                if count >= 3:
                    result.append([i-count, i-1])
                count = 1
        if count >= 3:
            result.append([len(s)-count, len(s)-1])
        return result