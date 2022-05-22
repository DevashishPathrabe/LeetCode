# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postOrder(root):
            if (not root):
                return
            postOrder(root.left)
            postOrder(root.right)
            self.result.append(root.val)
        self.result = []
        postOrder(root)
        return self.result