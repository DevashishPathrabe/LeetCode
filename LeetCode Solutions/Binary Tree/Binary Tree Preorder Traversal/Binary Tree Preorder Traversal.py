# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preOrder(root):
            if (not root):
                return
            self.result.append(root.val)
            preOrder(root.left)
            preOrder(root.right)        
        self.result = []
        preOrder(root)
        return self.result