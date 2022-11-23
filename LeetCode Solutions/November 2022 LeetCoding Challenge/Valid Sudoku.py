class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, boxMap = defaultdict(set), defaultdict(set), defaultdict(set)
        def getBoxIndex(r, c):
            return (r // 3) * 3 + (c // 3)
        for r in range(9):
            for c in range(9):
                number, boxIndex = str(board[r][c]), getBoxIndex(r, c)
                if number != '.':
                    if number in rowMap[r] or number in colMap[c] or number in boxMap[boxIndex]:
                        return False
                    rowMap[r].add(number)
                    colMap[c].add(number)
                    boxMap[boxIndex].add(number)
        return True