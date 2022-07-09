class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        numberOfBattleships = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    v = 1
                    if (r > 0 and board[r-1][c] == 'X') or (c > 0 and board[r][c-1] == 'X'):
                        v = 0
                    numberOfBattleships += v
        return numberOfBattleships