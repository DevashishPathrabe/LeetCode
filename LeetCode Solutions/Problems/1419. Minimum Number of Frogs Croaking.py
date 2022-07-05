class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        s = "croak"
        d = {c: 0 for c in s}
        prev = {s[i]: s[i - 1] for i in range(5)}
        for c in croakOfFrogs:
            if not d[prev[c]]:
                if c != 'c':
                    return -1
            else:
                d[prev[c]] -= 1
            d[c] += 1
        if any(d[c] for c in "croa"):
            return -1
        return d['k']