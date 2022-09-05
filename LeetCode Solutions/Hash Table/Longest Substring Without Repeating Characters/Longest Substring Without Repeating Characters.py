class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        temp = s[0]
        maxLength = 1
        for letter in s[1:]:
            if (letter in temp):
                i = temp.find(letter)
                temp = temp [i+1:]
            temp += letter
            if (len(temp) > maxLength):
                maxLength = len(temp)
        return maxLength