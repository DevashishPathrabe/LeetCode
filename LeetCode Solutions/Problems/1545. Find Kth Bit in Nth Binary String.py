class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        s = '011'
        for i in range(2, n):
            mid = len(s) // 2
            nw = s + '1' + s[:mid] + '0' + s[mid+1:]
            s = nw
        return s[k-1]