class Solution:
    def countTriples(self, n: int) -> int:
        s = set()
        for i in range(1,n+1):
            s.add(i*i)
        p = combinations(s,2)
        count = 0
        for i in p:
            if sum(list(i)) in s:
                count += 1
        return count * 2