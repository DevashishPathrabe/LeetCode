"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if (not root):
            return []
        levelOrderTraversal = []
        level = [root]
        while (level):
            levelOrderTraversal.append([node.val for node in level])
            level = [child for node in level for child in node.children if child]
        return levelOrderTraversal