# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### MY SOLN #########################################
class Solution:
    def mergeNodes(self, head):
        dummy = ListNode()
        temp = dummy
        cur = head
        while cur:
            sum = 0
            while cur and cur.next and cur.val:
                sum += cur.val
                cur = cur.next
            
            if sum:
                temp.next = ListNode(sum)
                temp = temp.next
            cur = cur.next

        return dummy.next

### OPTIMISED SOLN ##################################
class Solution:
    def mergeNodes(self, head):
        cur = head
        while cur:
            start = cur
            sum = 0
            while cur and cur.val:
                sum += cur.val
                cur = cur.next
            start.val = sum
            start.next = cur.next
            cur = cur.next
        return head.next

######################################################