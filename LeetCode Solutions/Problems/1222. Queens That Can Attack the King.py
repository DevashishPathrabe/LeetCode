class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        for d in directions:
            i, j = king[0], king[1]
            while 0 <= i <= 8 and 0 <= j <= 8:
                i += d[0]
                j += d[1]
                if [i, j] in queens:
                    result.append([i, j])
                    break
        return result