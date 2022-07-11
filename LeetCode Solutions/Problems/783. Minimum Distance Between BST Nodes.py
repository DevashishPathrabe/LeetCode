# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        List = []
        def inorder(root):
            if root:
                inorder(root.left)
                List.append(root.val)
                inorder(root.right)
        inorder(root)
        maximum = 10 ** 5
        for i in range(1, len(List)):
            if abs(List[i] - List[i - 1]) < maximum:
                maximum = abs(List[i] - List[i - 1])
        return maximum