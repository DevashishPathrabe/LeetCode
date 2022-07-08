class Solution:
    def numberOfWays(self, s: str) -> int:
        result = 0
        current1, current0, total1, total0 = 0, 0, 0, 0
        for bit in s:
            if bit == '1':
                total1 += 1
            else:
                total0 += 1
        if s[0] == '0':
            current0 += 1
        else:
            current1 += 1
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                current0 += 1
                result += current1 * (total1 - current1)
            else:
                current1 += 1
                result += current0 * (total0 - current0)
        return result