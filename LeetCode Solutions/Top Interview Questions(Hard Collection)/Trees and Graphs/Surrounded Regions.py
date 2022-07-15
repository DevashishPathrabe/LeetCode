class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(i, j):
            if(i>=0 and j>=0 and i<len(board) and j<len(board[0]) and board[i][j] == 'O'):
                board[i][j] = "#"
                helper(i+1, j)
                helper(i-1, j)
                helper(i, j+1)
                helper(i, j-1)
            else:
                return
        if(not board):
            return
        m = len(board)
        n = len(board[0])
        for row in range(m):
            helper(row, 0)
            helper(row, n-1)
        for column in range(1,n):
            helper(0, column)
            helper(m-1, column)
        for i in range(m):
            for j in range(n):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                elif(board[i][j] == "#"):
                    board[i][j] = "O"