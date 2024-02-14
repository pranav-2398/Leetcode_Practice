# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### MY SOLN ###########################################################################

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head.next:
#             head = None
#             return head

#         length = 0
#         temp = head
#         while temp:
#             temp = temp.next
#             length += 1

#         if n == length:
#             head = head.next
#             return head

        
#         prevnode = head
#         for _ in range(length - n - 1):
#             prevnode = prevnode.next

#         afternode = head
#         for _ in range(length - n + 1):
#             afternode = afternode.next

#         prevnode.next = afternode

#         return head
    
#######################################################################################

#### OPTIMISED SOLN ###################################################################
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next

#########################################################################################

s = Solution()
l = ListNode(1)
l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
# l.next.next.next.next = ListNode(5)
s.removeNthFromEnd(l, 2)
        