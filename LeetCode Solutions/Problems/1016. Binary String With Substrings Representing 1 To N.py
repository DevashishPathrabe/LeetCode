class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(s.find(bin(i)[2:]) != -1 for i in range(1, n + 1))