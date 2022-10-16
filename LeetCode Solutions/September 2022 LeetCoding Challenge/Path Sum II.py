# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        self.dfs(root, targetSum, [], paths)
        return paths
    def dfs(self, root, sum, curr_path, paths):
        curr_path.append(root.val)
        if root.val == sum and not (root.left or root.right):
            paths.append(curr_path)
        else:
            if root.left:
                self.dfs(root.left, sum-root.val, curr_path[:], paths)
            if root.right:
                self.dfs(root.right, sum-root.val, curr_path[:], paths)