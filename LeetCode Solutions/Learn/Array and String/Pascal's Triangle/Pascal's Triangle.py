class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows == 0):
            return []
        pascalTriangle = [[1]]
        pascalTriangle = pascalTriangle + [[1] * 2 for x in range(numRows-1)]
        for i in range(2, numRows):
            for j in range(1, i):
                pascalTriangle[i].insert(j, pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j])
        return pascalTriangle