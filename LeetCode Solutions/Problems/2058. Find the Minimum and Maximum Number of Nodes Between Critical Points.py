# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        previous = None
        temp = head
        minimum, maximum = 10 ** 5, 0
        count = 1
        difference = 10 ** 5
        while temp.next.next != None:
            previous = temp
            temp = temp.next
            count += 1
            if previous.val > temp.val < temp.next.val or previous.val < temp.val > temp.next.val:
                if maximum != 0:
                    minimum = min(minimum, count - maximum)
                difference = min(difference, count)
                maximum = count
        if difference == 10 ** 5 or minimum == 10 ** 5:
            return [-1, -1]
        return [minimum, maximum - difference]