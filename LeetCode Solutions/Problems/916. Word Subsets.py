class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2frequency = Counter()
        for word in words2:
            words2frequency |= Counter(word)
        if(sum(words2frequency.values()) > 10):
            return []
        return [word for word in words1 if(not words2frequency - Counter(word))]