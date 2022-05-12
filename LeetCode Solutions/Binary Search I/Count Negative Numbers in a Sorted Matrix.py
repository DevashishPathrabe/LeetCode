class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = sum(grid, [])
        count = 0
        for i in result:
            if i < 0:
                count +=1
        return count