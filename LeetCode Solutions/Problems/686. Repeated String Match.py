class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minLength = math.ceil(len(b) / len(a))
        for i in range(0, 2):
            if b in a * (minLength + i):
                return minLength + i
        return -1