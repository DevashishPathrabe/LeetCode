class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        p = ''
        for i in b:
            p += str(i)
        p = int(p)
        return pow(a, p, mod)