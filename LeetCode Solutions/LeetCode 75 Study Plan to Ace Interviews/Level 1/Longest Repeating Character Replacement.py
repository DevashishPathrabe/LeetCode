class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = defaultdict(int)
        i, j = 0, 0
        result = 0
        while j < len(s):
            mapping[s[j]] += 1
            while sum(mapping.values()) - max(mapping.values()) > k:
                mapping[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
            j += 1
        return result