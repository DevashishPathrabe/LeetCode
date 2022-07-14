# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        pointer = None
        def helper(node, cnode):
            nonlocal pointer
            if(not node or pointer):
                return
            if(node == target):
                pointer = cnode
                return
            helper(node.left, cnode.left)
            helper(node.right, cnode.right)
        helper(original, cloned)
        return pointer