class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        for i in words1:
            if freq1[i] == 1 and freq2[i] == 1:
                count += 1
        return count