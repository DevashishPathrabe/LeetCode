class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = len(words)
        helper = set(allowed)
        for j in words:
            for vowel in j:
                if vowel not in helper:
                    result -= 1
                    break
        return result