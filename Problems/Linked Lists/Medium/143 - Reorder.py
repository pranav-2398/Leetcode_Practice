# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
### MY SOLN (TIME EXCESS) #####################################
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         curr = head
#         while curr.next:
#             nxt = curr.next
#             last = nxt
#             prev = curr
#             while last.next:
#                 last = last.next
#                 prev = prev.next
            
#             if last:
#                 curr.next = last
#                 last.next = nxt
#                 prev.next = None
#                 curr = nxt
#             else:
#                 break
#################################################################
        
### OPTIMUM SOLN ################################################
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        #Finding the middle of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = prev = None

        #Reversing 2nd half of list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #Merge 2 halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

####################################################################

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s.reorderList(head)

