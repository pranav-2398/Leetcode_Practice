from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            if prev and prev.val == temp.val:
                while temp and prev.val == temp.val:
                    temp = temp.next
                prev.next = temp
            prev = temp
            temp = temp.next if temp else None
        return head