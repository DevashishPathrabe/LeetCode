class Solution:
    def magicalString(self, n: int) -> int:
        s = '122'
        i = 2
        bl = True
        while len(s) <= n:
            if s[i] == '1':
                s += '1' if bl else '2'
            else:
                s += '11' if bl else '22'
            i += 1
            if bl:
                bl = False
            else:
                bl = True

        c = collections.Counter(s[:n])
        return c['1']