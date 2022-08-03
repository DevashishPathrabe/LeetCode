"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def populate(root, i):
            if (root):
                if (i in nodes):
                    nodes[i].next = root
                    nodes[i] = root
                else:
                    nodes[i] = root
                populate(root.left, i+1)
                populate(root.right, i+1)
        nodes = {}
        populate(root, 0)
        return root