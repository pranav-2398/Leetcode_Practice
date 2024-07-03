# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        stack = []
        setx = set()
        cur = head

        while cur:
            if cur.val in setx:
                while stack and stack[-1].val == cur.val:
                    stack.pop()
                if stack:
                    stack[-1].next = cur.next
            else:
                setx.add(cur.val)
                stack.append(cur)
            cur = cur.next
        
        return stack[0] if stack else None