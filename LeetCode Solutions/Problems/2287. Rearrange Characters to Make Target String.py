class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        return min([Counter(s)[ch] // Counter(target)[ch] for ch in target])