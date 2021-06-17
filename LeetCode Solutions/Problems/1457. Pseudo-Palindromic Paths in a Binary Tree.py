# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode, mask = 0) -> int:
        mask = mask ^ (1 << root.val)
        if(root.left and root.right):
            return self.pseudoPalindromicPaths(root.left, mask) + self.pseudoPalindromicPaths(root.right, mask)
        elif(root.left or root.right):
            return self.pseudoPalindromicPaths(root.left, mask) if root.left else self.pseudoPalindromicPaths(root.right, mask)
        return int(bin(mask).count('1') <= 1)