class Solution:
    def countVowels(self, word: str) -> int:
        vowel = "aeiou"
        n, result = len(word), 0
        for i, c in enumerate(word):
            if c in vowel:
                result += (n-i)*(i+1)
        return result