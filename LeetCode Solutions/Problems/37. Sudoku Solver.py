class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(i, j, value):
            for k in range(len(board)):
                if(board[k][j] == value or board[i][k] == value):
                    return False
            regionSize = int(math.sqrt(len(board)))
            I = i // regionSize
            J = j // regionSize
            return not any(value == board[regionSize*I + a][regionSize*J + b] for a, b in itertools.product(range(regionSize), repeat = 2))
        def solvePartialSudoku(i, j):
            if(i == len(board)):
                i = 0
                j += 1
                if(j == len(board)):
                    return True
            if(board[i][j] != '.'):
                return solvePartialSudoku(i+1, j)
            for value in range(1, len(board)+1):
                if(valid(i, j, str(value))):
                    board[i][j] = str(value)
                    if(solvePartialSudoku(i+1,j)):
                        return True
            board[i][j] = '.'
            return False
        solvePartialSudoku(0,0)