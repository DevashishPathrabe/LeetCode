class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = collections.Counter()
        for i in range(len(s)):
            key = s[i:i+10]
            counts[key] += 1
        return [i[0] for i in counts.items() if i[1] > 1]