class Solution:
    def minOperations(self, s: str) -> int:
        even, odd = [], []
        for i in range(len(s)):
            if i % 2 == 0:
                even.append(s[i])
            else:
                odd.append(s[i])
        return min(even.count('1') + odd.count('0'), even.count('0') + odd.count('1'))