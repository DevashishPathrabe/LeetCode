# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        Sum = 0
        stack = [root]
        while(stack):
            current = stack.pop()
            if(current):
                if(current.left):
                    stack.append(current.left)
                    if(current.left.left is None and current.left.right is None):
                        Sum += current.left.val
                if(current.right):
                    stack.append(current.right)
        return Sum