class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        citations.reverse()
        for i, cit in enumerate(citations):
            if cit <= i:
                return i
        return len(citations)