class Solution:
    def secondHighest(self, s: str) -> int:
        u = set()
        for i in s:
            if i.isdigit() and i not in u:
                u.add(i)
        if len(u) < 2:
            return -1
        return sorted(list(u))[-2]