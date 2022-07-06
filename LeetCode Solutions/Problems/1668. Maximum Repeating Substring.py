class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        resword = ''
        while True:
            resword = resword + word
            value = sequence.find(resword)
            if value == -1:
                break
            else:
                count += 1
        return count