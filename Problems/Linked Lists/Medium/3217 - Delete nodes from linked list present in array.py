from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## MY SOLN ##################################################################################
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None    
        nums = set(nums)
        def helper(root):
            nonlocal temp
            if not root:
                return None
            root.next = helper(root.next)
            if root.val not in nums:
                root.next = temp
                temp = root
            else:
                root = None
            return root
        head = helper(head)

        return head if head else temp
## ANOTHER SOLN #############################################################################
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = dummy
        nums = set(nums)
        while cur.next:
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
#############################################################################################
            