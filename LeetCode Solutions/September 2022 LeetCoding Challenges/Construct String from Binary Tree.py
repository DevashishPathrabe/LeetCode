# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return ""
            else:
                l = preorder(node.left)
                r = preorder(node.right)
                if l == '' and r == '':
                    return str(node.val)
                elif r == '':
                    return str(node.val) + '(' + l + ')'
                else:
                    return str(node.val) + '(' + l + ')' + '(' + r + ')'
        return preorder(root)