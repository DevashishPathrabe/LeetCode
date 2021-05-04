class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        if(matrix):
            previous = [0] * len(matrix[0])
            for row in matrix:
                s = [1 if(i == '1') else 0 for i in row]
                for j in range(1, len(s)):
                    if(s[j]):
                        s[j] = min(previous[j-1], previous[j], s[j-1]) + 1
                area = max(area, max(s)**2)
                previous = s
        return area