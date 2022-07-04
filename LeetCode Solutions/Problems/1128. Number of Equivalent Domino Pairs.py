class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter(min(d) + 10 * max(d) for d in dominoes)
        return sum(c*(c-1)//2 for c in counts.values())