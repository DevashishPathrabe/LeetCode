# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        sumNodes = 0
        while(stack):
            node = stack.pop()
            if(node):
                if(low <= node.val <= high):
                    sumNodes += node.val
                    if(node.right):
                        stack.append(node.right)
                    if(node.left):
                        stack.append(node.left)
                elif(node.val < low and node.right):
                    stack.append(node.right)
                elif(node.val > high and node.left):
                    stack.append(node.left)
        return sumNodes