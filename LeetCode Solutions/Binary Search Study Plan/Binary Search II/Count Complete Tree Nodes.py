# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(node):
            result = 0
            while(node):
                result += 1
                node = node.left
            return result
        def numberOfNodes(node):
            result = 0
            while(node):
                left = height(node.left)
                right = height(node.right)
                if(left == right):
                    result += 1 + 2**left - 1
                    node = node.right
                else:
                    result += 1 + 2**right - 1
                    node = node.left
            return result
        return numberOfNodes(root)