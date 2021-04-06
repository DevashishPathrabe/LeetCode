# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, previous = head, head, None
        while(fast and fast.next):
            slow, fast = slow.next, fast.next.next
        previous, slow, previous.next = slow, slow.next, None
        while(slow):
            temp = slow.next
            slow.next, previous, slow = previous, slow, temp
        fast, slow = head, previous
        while(slow):
            if(fast.val != slow.val):
                return False
            fast, slow = fast.next, slow.next
        return True