"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x, y, size):
            if size == 1:
                return Node(grid[x][y], True, None, None, None, None)
            half = size // 2
            topLeft = helper(x, y, half)
            topRight = helper(x, y + half, half)
            bottomLeft = helper(x + half, y, half)
            bottomRight = helper(x + half, y + half, half)
            children = [topLeft, topRight, bottomLeft, bottomRight]
            allLeaves = all(c.isLeaf for c in children)
            allMatch = all(c.val == topLeft.val for c in children)
            isLeaf = allLeaves and allMatch
            if isLeaf:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        return helper(0, 0, len(grid))