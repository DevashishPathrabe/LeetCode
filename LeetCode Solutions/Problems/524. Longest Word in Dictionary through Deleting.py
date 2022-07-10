class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longestString = ""
        for word in dictionary:
            wordLength, stringLength = len(word), len(longestString)
            if(wordLength < stringLength or (wordLength == stringLength and word > longestString)):
                continue
            position = -1
            for char in word:
                position = s.find(char, position + 1)
                if(position == -1):
                    break
            if(position != -1):
                longestString = word
        return longestString