# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(node = root, level = 0):
            if not node:
                return
            if len(result)-1 < level:
                result.append(node.val)
            else:
                result[level] = max(node.val, result[level])
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper()
        return result