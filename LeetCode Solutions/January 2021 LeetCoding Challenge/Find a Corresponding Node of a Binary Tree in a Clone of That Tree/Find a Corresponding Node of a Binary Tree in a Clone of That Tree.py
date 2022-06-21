# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(realNode, clonedNode):
            if (not realNode):
                return None
            if (realNode == target):
                return clonedNode
            return traverse(realNode.left, clonedNode.left) or traverse(realNode.right, clonedNode.right)
        return traverse(original, cloned)