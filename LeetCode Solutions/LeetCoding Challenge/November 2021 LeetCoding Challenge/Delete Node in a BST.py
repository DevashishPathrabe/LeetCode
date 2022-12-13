# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if(root):
            if(key > root.val):
                root.right = self.deleteNode(root.right, key)
            elif(key < root.val):
                root.left = self.deleteNode(root.left, key)
            elif(not root.right):
                return root.left
            elif(not root.right.left):
                root.right.left = root.left
                return root.right
            else: 
                parent = rightSmallest = root.right
                while(rightSmallest.left):
                    parent = rightSmallest
                    rightSmallest = rightSmallest.left
                root.val = rightSmallest.val
                parent.left = rightSmallest.right
        return root