class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        numberOfFriendCircles = 0
        def dfs(row, n):
            for j in range(n):
                if(M[row][j] == 1):
                    M[row][j] = M[j][row] = -1
                    dfs(j, n)
        for row in range(n):
            if(M[row][row] == 1):
                numberOfFriendCircles += 1
                dfs(row, n)
        return numberOfFriendCircles