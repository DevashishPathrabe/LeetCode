# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level, ansLevel, ansSum = 0, 0, float('-inf')
        q = deque([root])
        while q:
            level += 1
            Sum = 0
            for _ in range(len(q)):
                x = q.popleft()
                Sum += x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            if Sum > ansSum:
                ansLevel, ansSum = level, Sum
        return ansLevel