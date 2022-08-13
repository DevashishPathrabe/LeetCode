class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l, s_len, word_len, words_len = 0, len(s), len(words[0]), len(words)
        concat_len = word_len*words_len
        words_counter, res = Counter(words), []
        for r in range(concat_len-1, s_len):
            seen = Counter()
            for k in range(l,r+1,word_len):
                word = s[k:k+word_len]
                seen[word] += 1
                if words_counter[word] < seen[word]:
                    break
            else:
                res.append(l)
            l += 1
        return res