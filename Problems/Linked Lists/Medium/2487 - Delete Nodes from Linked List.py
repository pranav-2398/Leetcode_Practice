from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##### STACK SOLN ##########################################################       
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            while stack and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next

        dummy = ListNode()
        cur = dummy
        for n in stack:
            cur.next = ListNode(n)
            cur = cur.next
        
        return dummy.next

#### Recursion ##############################################################
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case, reached end of the list
        if head is None or head.next is None:
            return head

        # Recursive call
        next_node = self.removeNodes(head.next)
        
        # If the next node has greater value than head, delete the head
        # Return next node, which removes the current head and 
        # makes next the new head
        if head.val < next_node.val:
            return next_node
     
        # Keep the head
        head.next = next_node
        return head

####### Reverse the list #####################################################
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            return prev
        
        head = reverse(head)
        cur = head
        cur_max = cur.val
        while cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur_max = cur.next.val
                cur = cur.next
        return reverse(head)
############################################################################