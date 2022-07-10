class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        i = 0
        lengths = defaultdict(int)
        mapping = {chr(i + 97):chr((i + 1)%26 + 97) for i in range(26)}
        while i < len(p):
            j = i + 1
            while j < len(p) and p[j] == mapping[p[j - 1]]:
                j += 1
            l = j - i
            for i in range(i, j):
                if lengths[p[i]] < l:
                    lengths[p[i]] = l
                    l -= 1
                else:
                    break
            i = j
        return sum(lengths.values())