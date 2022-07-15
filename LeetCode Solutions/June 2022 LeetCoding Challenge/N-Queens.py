class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        distinctSolutions = []
        board = [['.'] * n for _ in range(n)]
        def place(i: int, vertical: int, leftdiagonal: int, rightdiagonal:int) -> None:
            if(i == n):
                distinctSolutions.append(["".join(row) for row in board])
                return
            for j in range(n):
                vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (n-i-1+j)
                if(vertical & vmask or leftdiagonal & lmask or rightdiagonal & rmask):
                    continue
                board[i][j] = 'Q'
                place(i+1, vertical | vmask, leftdiagonal | lmask, rightdiagonal | rmask)
                board[i][j] = '.'
        place(0,0,0,0)
        return distinctSolutions