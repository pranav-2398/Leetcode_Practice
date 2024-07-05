from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        dist = []

        i = 1
        cur = head
        prev = None

        while cur and cur.next:
            if prev and (
                (prev.val < cur.val and cur.val > cur.next.val) or 
                (prev.val > cur.val and cur.val < cur.next.val)
                ):
                dist.append(i)
            prev = cur
            cur = cur.next
            i += 1

        if len(dist) < 2:
            return res

        res[1] = dist[-1] - dist[0]

        minval = float('inf')
        for i in range(0, len(dist) - 1):
            minval = min(minval, dist[i + 1] - dist[i])
        
        res[0] = minval

        return res