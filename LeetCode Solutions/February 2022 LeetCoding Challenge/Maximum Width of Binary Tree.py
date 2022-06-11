# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(root,1)]
        result = 1
        lastnode = root
        while len(q):
            node,index = q.pop(0)
            if node.left:
                q.append((node.left,2*index))
            if node.right:
                q.append((node.right,2*index+1))
            if node == lastnode:
                if len(q):
                    result = max(result,q[-1][1] - q[0][1] + 1)
                    lastnode = q[-1][0]
        return result