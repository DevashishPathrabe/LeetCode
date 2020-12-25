"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head is None):
            return None 
        dict = {}
        curr = head
        while(curr):
            dict[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while(curr):
            if(curr.next != None):
                dict[curr].next = dict[curr.next]
            if(curr.random != None):
                dict[curr].random = dict[curr.random]
            curr = curr.next
        return dict[head]
