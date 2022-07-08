class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        for i in range(len(word) - 4):
            v_l = ['a','e', 'i', 'o', 'u']
            if word[i] in v_l:
                track = set([word[i]])
                for j in range(i+1, len(word)):
                    if word[j] not in v_l:
                        break
                    track.add(word[j])
                    if len(track) == 5:
                        result += 1
        return result