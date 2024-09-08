from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1
        
        baselen, rem = length // k, length % k
        cur = head
        res = []

        for i in range(k):
            res.append(cur)

            for j in range(baselen - 1 + (1 if rem else 0)):
                if not cur:
                    break
                cur = cur.next
            rem -= (1 if rem else 0)

            if cur:
                cur.next, cur = None, cur.next
        
        return res

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)

print(s.splitListToParts(head, 3))