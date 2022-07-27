# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head, current = None, root
        while(head != root):
            if(current.right == head):
                current.right = None
            if(current.left == head):
                current.left = None
            if(current.right):
                current = current.right
            elif(current.left):
                current = current.left
            else:
                current.right, head, current = head, current, root