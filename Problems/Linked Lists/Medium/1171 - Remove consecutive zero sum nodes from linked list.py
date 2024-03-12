# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixSum = 0
        mp = {}
        dummy = ListNode(0)
        dummy.next = head
        mp[0] = dummy
        while head:
            prefixSum += head.val
            if prefixSum in mp:
                start = mp[prefixSum]
                temp = start
                pSum = prefixSum
                while temp != head:
                    temp = temp.next
                    pSum += temp.val
                    if temp != head:
                        del mp[pSum]
                start.next = head.next
            else:
                mp[prefixSum] = head
            head = head.next
        return dummy.next
            
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

s = Solution()
print(s.removeZeroSumSublists(head))