class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s, count = str(num), 0
        for i in range(len(s) - k + 1):
            temp = int(s[i : i + k])
            if temp != 0 and num % temp == 0:
                count += 1
        return count