from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### MY SOLN (BUT RUNTIME ERROR DUE TO TOO MANY DIGITS FOR INT TO STR CONVERSION)#####
# class Solution:
#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         no = ''
#         cur = head
#         while cur:
#             no += str(cur.val)
#             cur = cur.next
#         no = str(int(no) * 2)
#         dummy = ListNode()
#         temp = dummy
#         for s in no:
#             temp.next = ListNode(int(s))
#             temp = temp.next
#         return dummy.next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            return prev
        
        head = reverse(head)

        cur, prev = head, None
        carry = 0
        while cur:
            sumval = (cur.val * 2 + carry)
            cur.val = sumval % 10
            carry = sumval // 10
            prev, cur = cur, cur.next

        if carry:
            prev.next = ListNode(carry)
        
        return reverse(head)
    
head = ListNode(1)
head.next =ListNode(8)
head.next.next = ListNode(9)
s = Solution()
print(s.doubleIt(head).val)