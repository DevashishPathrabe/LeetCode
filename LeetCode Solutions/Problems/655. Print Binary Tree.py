# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        h = self.height(root)
        matrix = [['' for n in range((2 ** h) - 1)] for m in range(h)]
        self.place(root, matrix, 0, (2 ** h) - 1, 0)
        return matrix
    def height(self, node):
        if node:
            return max(1 + self.height(node.left), 1 + self.height(node.right))
        else:
            return 0
    def place(self, node, matrix, i, j, row):
        if node:
            col = (i + j) // 2
            matrix[row][col] = str(node.val)
            self.place(node.left, matrix, i, col, row + 1)
            self.place(node.right, matrix, col + 1, j, row + 1)