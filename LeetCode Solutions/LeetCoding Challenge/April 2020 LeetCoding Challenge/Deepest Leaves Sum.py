# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q, Sum, current = [root], 0, 0
        while(len(q)):
            Sum = 0
            for _ in range(len(q)):
                current = q.pop(0)
                Sum += current.val
                if(current.left):
                    q.append(current.left)
                if(current.right):
                    q.append(current.right)
        return Sum