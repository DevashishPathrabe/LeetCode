class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        numberOfFriendCircles = 0
        def dfs(row, n):
            for j in range(n):
                if (isConnected[row][j] == 1):
                    isConnected[row][j] = isConnected[j][row] = -1
                    dfs(j, n)
        for row in range(n):
            if (isConnected[row][row] == 1):
                numberOfFriendCircles += 1
                dfs(row, n)
        return numberOfFriendCircles