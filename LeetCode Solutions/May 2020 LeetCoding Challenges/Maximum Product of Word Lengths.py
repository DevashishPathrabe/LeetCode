class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        maximumValue, bitsets = 0, {}
        for i in range(len(words)):
            wlen, bitset = len(words[i]), 0
            if(wlen * len(words[0]) < maximumValue):
                return maximumValue
            for c in words[i]:
                bitset |= 1 << ord(c) - 97
            if(bitset not in bitsets):
                for k,v in bitsets.items():
                    if(not bitset & k):
                        maximumValue = max(maximumValue, wlen * v)
                bitsets[bitset] = wlen
        return maximumValue