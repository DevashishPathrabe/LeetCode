class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [poured]
        for _ in range(query_row):
            new = [0] * (len(cups) + 1) 
            for j in range(len(cups)):
                give = max(0, cups[j] - 1) / 2. 
                new[j] += give
                new[j+1] += give
            cups = new
        return min(1, cups[query_glass])