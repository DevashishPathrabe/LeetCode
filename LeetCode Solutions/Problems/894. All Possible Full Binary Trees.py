# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode()]
        for i in range(1, n + 1, 2):
            for j in range(1, i, 2):
                for tree1 in dp[j]:
                    for tree2 in dp[i - j - 1]:
                        dp[i].append(TreeNode(0, tree1, tree2))
        return dp[-1]