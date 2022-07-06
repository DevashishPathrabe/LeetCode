# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def helper(node, depth, maxDist):
            if not node:
                return []
            if not node.left and not node.right:
                return [depth]
            leftLeaves = helper(node.left, depth + 1, maxDist)
            rightLeaves = helper(node.right, depth + 1, maxDist)
            for left in leftLeaves:
                for right in rightLeaves:
                    if left + right - 2*depth <= maxDist:
                        self.result += 1
            return leftLeaves + rightLeaves
        helper(root, 0, distance)
        return self.result