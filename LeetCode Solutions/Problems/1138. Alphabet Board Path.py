class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        size = 5
        current_x, current_y = 0, 0
        offset = ord('a')
        ans = ''
        for i in target:
            row = (ord(i) - offset) // size
            col = (ord(i) - offset) % size
            if current_x > col:
                ans += 'L' * (current_x - col)
            if row > current_y:
                ans += 'D' * (row - current_y)
            if current_y > row:
                ans += 'U' * (current_y - row)    
            if col > current_x:
                ans += 'R' * (col - current_x)
            ans += '!'
            current_x, current_y = col, row
        return ans