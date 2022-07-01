class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        Bfrequency = Counter()
        for word in B:
            Bfrequency |= Counter(word)
        if(sum(Bfrequency.values()) > 10):
            return []
        return [word for word in A if(not Bfrequency - Counter(word))]