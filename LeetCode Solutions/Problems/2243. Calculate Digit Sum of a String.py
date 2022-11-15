class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            string = ''
            for i in range(0, len(s), k):
                string += str(sum([int(c) for c in s[i:i+k]]))
            s = string[:]
        return s