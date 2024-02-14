# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #### MY ORIGINAL SOLN #################################################################

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     start1 = headA
    #     start2 = headB
    #     cache = {}

    #     while start1:
    #         cache[start1] = 1
    #         start1 = start1.next

    #     while start2:
    #         if start2 in cache:
    #             return start2
    #         start2 = start2.next

    #     return None
    
    ##########################################################################################

    ###### OPTIMISED SOLN ####################################################################

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1
    
    ############################################################################################


    
s = Solution()

l1 = ListNode(1)
l2 = l1

x = s.getIntersectionNode(l1, l2)

print(x)