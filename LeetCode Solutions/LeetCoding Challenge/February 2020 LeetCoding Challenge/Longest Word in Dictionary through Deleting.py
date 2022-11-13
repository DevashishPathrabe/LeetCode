class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longestString = ""
        for word in d:
            a, b = len(word), len(longestString)
            if(a < b or (a == b and word > longestString)):
                continue
            position = -1
            for char in word:
                position = s.find(char, position + 1)
                if(position == -1):
                    break
            if(position != -1):
                longestString = word
        return longestString