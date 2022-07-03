# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(not root):
            return []
        q = deque()
        q.append(root)
        levels = []
        oneLevel = []
        while(len(q) != 0):
            for i in range(len(q)):
                popped = q.popleft()
                oneLevel.append(popped.val)
                if(popped.left):
                    q.append(popped.left)
                if(popped.right):
                    q.append(popped.right)
            levels.append(oneLevel)
            oneLevel = []
        return levels