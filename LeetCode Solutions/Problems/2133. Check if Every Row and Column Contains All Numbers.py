class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(0, len(matrix)):
            map = set()
            for j in range(0, len(matrix)):
                map.add(matrix[i][j])
            if len(map) != n:
                return False
        for i in range(0, len(matrix)):
            map = set()
            for j in range(0, len(matrix)):
                map.add(matrix[j][i])
            if len(map) != n:
                return False
        return True