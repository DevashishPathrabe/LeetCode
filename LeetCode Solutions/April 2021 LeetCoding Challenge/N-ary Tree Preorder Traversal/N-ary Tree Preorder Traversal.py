"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if (not root):
            return []
        resultTree = [root.val]
        if (root.children):
            for child in root.children:
                resultTree += self.preorder(child)
        return resultTree