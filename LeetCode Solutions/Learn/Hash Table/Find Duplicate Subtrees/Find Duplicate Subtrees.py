# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        duplicateSubtrees = []
        seen = {}
        self.helper(root, seen, duplicateSubtrees)
        return duplicateSubtrees
    def helper(self, node, seen, duplicateSubtrees):
        if (not node):
            return '*'
        current = str(node.val)
        left = self.helper(node.left, seen, duplicateSubtrees)
        right = self.helper(node.right, seen, duplicateSubtrees)
        p = '%s, %s, %s' % (current, left, right)
        if (p not in seen):
            seen[p] = 1
        else:
            seen[p] += 1
        if (seen[p] == 2):
            duplicateSubtrees.append(node)
        return p