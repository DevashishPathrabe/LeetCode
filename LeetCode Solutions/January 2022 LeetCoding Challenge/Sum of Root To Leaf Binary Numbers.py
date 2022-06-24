# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    Sum = 0
    SumString = []
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if (not root):
            return
        self.SumString.append(str(root.val))
        if(not root.left and not root .right):
            self.Sum += int(''.join(self.SumString), 2)
        self.sumRootToLeaf(root.left)
        self.sumRootToLeaf(root.right)
        self.SumString.pop(-1)
        return self.Sum