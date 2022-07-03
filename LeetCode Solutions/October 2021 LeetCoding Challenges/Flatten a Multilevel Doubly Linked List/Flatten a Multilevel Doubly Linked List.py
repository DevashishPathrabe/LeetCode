"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if (head == None):
            return None
        stack = [head]
        previousNode = None
        while len(stack) > 0:
            currentNode = stack.pop()
            if (currentNode.next):
                stack.append(currentNode.next)
            if (currentNode.child):
                stack.append(currentNode.child)
            if (previousNode):
                previousNode.next = currentNode
                currentNode.prev = previousNode
            currentNode.child = None
            previousNode = currentNode
        return head