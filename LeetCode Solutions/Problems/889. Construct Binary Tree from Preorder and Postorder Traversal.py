# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            x = postorder.pop()
            preorder.pop(0)
            root = TreeNode(x)
            p = 0
            while preorder and preorder[p] != postorder[-1]:
                p += 1
            pre_left= preorder[:p]; post_left = postorder[:p]
            pre_right = preorder[p:]; post_right = postorder[p:]
            l = self.constructFromPrePost(pre_left, post_left)
            r = self.constructFromPrePost(pre_right, post_right)
            root.left = l 
            root.right = r
            return root
        return None