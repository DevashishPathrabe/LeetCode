"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if(root):
            temp = [self.maxDepth(child) for child in root.children]
            if(temp == []):
                return  1
            else:
                depth = 1 + max(temp)
                return depth
        else:
            return 0