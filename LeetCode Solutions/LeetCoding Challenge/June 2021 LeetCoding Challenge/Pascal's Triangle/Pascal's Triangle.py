class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        firstNumRows = [None] * numRows
        for i in range(numRows):
            row, middle = [1] * (i + 1), (i >> 1) + 1
            for j in range(1, middle):
                val = firstNumRows[i-1][j-1] + firstNumRows[i-1][j]
                row[j], row[len(row)-j-1] = val, val
            firstNumRows[i] = row
        return firstNumRows