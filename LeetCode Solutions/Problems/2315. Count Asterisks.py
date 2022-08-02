class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '|' and flag == 0:
                flag = 1
            elif s[i] == '|' and flag == 1:
                flag = 0
            elif s[i] == '*' and flag == 0:
                count += 1
        return count