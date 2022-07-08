class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(list)
        numberOfRods = 0
        for i in range(1, len(rings), 2):
            if rings[i-1] not in d[rings[i]]:
                d[rings[i]].append(rings[i-1])
        for i in d:
            if ['B', 'G', 'R'] == sorted(d[i]):
                numberOfRods += 1
        return numberOfRods