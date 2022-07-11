class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for s in cpdomains:
            count, s = s.split()
            count = int(count)
            d[s] += count
            position = s.find('.') + 1
            while position > 0:
                d[s[position:]] += count
                position = s.find('.', position) + 1
        for x, i in d.items():
            yield f'{i} {x}'