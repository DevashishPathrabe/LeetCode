# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q = []
        q.append(root)
        result = []
        while q:
            temp=[]
            for _ in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if temp:
                result.append(temp)
        return result[::-1]