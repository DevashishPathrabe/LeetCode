# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dqueue = deque()
        dqueue.append(root)
        while dqueue:
            currentNode = dqueue.popleft()
            if currentNode:
                if currentNode.right:
                    dqueue.append(currentNode.right)
                if currentNode.left:
                    dqueue.append(currentNode.left)
        return(currentNode.val)