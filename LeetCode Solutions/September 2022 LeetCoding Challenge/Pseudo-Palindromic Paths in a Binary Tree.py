# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        paths = []
        def traverse(root, path):
            if root:
                if root.val in path:
                    path[root.val] += 1
                else:
                    path[root.val] = 1
                if root.left is None and root.right is None:
                    odds = 0
                    for val in path.values():
                        if val ^ (val-1) == 1:
                            odds += 1
                    if odds == 1 or odds == 0:
                        paths.append(path)
                traverse(root.left, path.copy())
                traverse(root.right, path.copy())
            return
        traverse(root, {})
        return len(paths)