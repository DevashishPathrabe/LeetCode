class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, column = -1, -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row, column = i, j
        result = 0
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        for dd in d:
            rr, cc = row, column
            while rr+dd[0] > -1 and rr+dd[0] < 8 and cc+dd[1] > -1 and cc+dd[1] < 8:
                rr += dd[0]
                cc += dd[1]
                if board[rr][cc] == 'p':
                    result += 1
                if board[rr][cc] != '.':
                    break
        return result