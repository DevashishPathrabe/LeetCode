class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = []
        mod = len(s) % k
        if mod :
            s = s + (k-mod) * fill
        i = 0
        j = k
        while j <= len(s):
            arr.append(s[i:j])
            i += k
            j += k
        return arr