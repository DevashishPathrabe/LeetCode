class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = bin(n)[2:]
        complement = 0
        for i in range(len(x)):
            if x[i] == '0':
                complement += 2 ** (len(x) - i - 1)
        return complement