class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        d = [[0] * length for j in range(64)]
        for i in range(length - 2, -1, -1):
            piles[i] += piles[i + 1]
        def find(m, current):
            if length - current <= m * 2:
                return piles[current]
            if d[m][current]:
                return d[m][current]
            minCount = sys.maxsize
            for x in range(1, m * 2 + 1):
                count = find(max(x, m), current + x)
                if count < minCount:
                    minCount = count
            d[m][current] = piles[current] - minCount
            return piles[current] - minCount
        return find(1, 0)