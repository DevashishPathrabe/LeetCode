class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        w = len(matrix[0])
        h = len(matrix)
        result = 0
        for y in range(h):
            for x in range(w):
                if matrix[y][x]:
                    if y > 0 and x > 0:
                        matrix[y][x] += min(matrix[y][x-1], matrix[y-1][x-1], matrix[y-1][x])
                    result += matrix[y][x]
        return result