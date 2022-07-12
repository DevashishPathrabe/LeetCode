"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head is None):
            return None
        dict = {}
        current = head
        while(current):
            dict[current] = Node(current.val, None, None)
            current = current.next
        current = head
        while(current):
            if(current.next != None):
                dict[current].next = dict[current.next]
            if(current.random != None):
                dict[current].random = dict[current.random]
            current = current.next
        return dict[head]