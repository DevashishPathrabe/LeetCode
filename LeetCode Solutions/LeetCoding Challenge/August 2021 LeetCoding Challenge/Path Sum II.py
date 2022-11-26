# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.output = []
        def helper(node, path):
            if not node:
                return None
            if not node.left and not node.right:
                if sum(path + [node.val]) == targetSum:
                    self.output.append(path + [node.val])
                return
            helper(node.left, path + [node.val])
            helper(node.right, path + [node.val])
        helper(root, [])
        return self.output