# # Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


############# ORIGINAL SOLN #######################################################################
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = val2 = 0
        i = 0
        j = 0

        while l1:
            val1 += 10**i * l1.val
            i += 1
            l1 = l1.next

        while l2:
            val2 += 10**j * l2.val
            j += 1
            l2 = l2.next
        
        val3 = val1 + val2

        l3 = ListNode()
        temp = l3

        while val3 != 0:
            num = val3 % 10
            temp.next = ListNode(num)
            val3 = val3 // 10
            temp = temp.next
        
        if l3.next:
            l3 = l3.next

        return l3

##################################################################################################
    
############### NEW SOLN #########################################################################

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = val2 = 0
        i = 0
        j = 0

        l3 = ListNode()
        temp = l3

        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10

            temp.next = ListNode(val)
            temp = temp.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            temp.next = ListNode(l1.val)
            temp = temp.next
            l1 = l1.next
        
        while l2:
            temp.next = ListNode(l2.val)
            temp = temp.next
            l2 = l2.next
        
        if l3.next:
            l3 = l3.next
        
        return l3
    
##### SYNATICALLY BETTER SOLN ###############################################################
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        temp = dummy
        while l1 != None or l2 != None or carry != 0:
            sum = 0
            if l1!= None :
                sum += l1.val 
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum//10
            node = ListNode(sum%10)
            temp.next = node
            temp = temp.next
        return dummy.next
############################################################################################





            



s = Solution()
l1 = ListNode(0)
l2 = ListNode(0)

print(s.addTwoNumbers(l1, l2))
        
print(0 // 10)