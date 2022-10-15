# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, averageValue = [root], []
        while(len(queue)):
            queueLength, row = len(queue), 0
            for i in range(queueLength):
                current = queue.pop(0)
                row += current.val
                if(current.left):
                    queue.append(current.left)
                if(current.right):
                    queue.append(current.right)
            averageValue.append(row/queueLength)
        return averageValue