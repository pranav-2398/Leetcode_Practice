# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         dummy = ListNode()
#         # temp = head
#         prev = dummy
#         while head:
#             start = head
#             n = k
#             nodelist = []
#             while start and n > 0:
#                 nodelist.append(start)
#                 start = start.next
#                 n -= 1
#             if n:
#                 break
#             next = start
#             prev.next = nodelist[-1]
#             for i in range(k-1, 0, -1):
#                 nodelist[i].next = nodelist[i - 1]
#             nodelist[0].next = next
#             prev = nodelist[0]
#             head = next

#         return dummy.next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # temp = head
        groupprev = dummy
        while True:
            kth = self.getKth(groupprev, k)
            if not kth:
                break
            groupnext = kth.next

            prev, curr = kth.next, groupprev.next

            while curr != groupnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp

        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s.reverseKGroup(head, 2)



