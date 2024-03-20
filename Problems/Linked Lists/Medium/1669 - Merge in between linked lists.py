# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = list1

        slow = fast = dummy
        for _ in range(b-a + 1):
            fast = fast.next

        for _ in range(a):
            slow = slow.next
            fast = fast.next

        slow.next = list2
        temp = list2
        while temp.next:
            temp = temp.next
        
        temp.next = fast.next
        return dummy.next

list1 = ListNode(10)
list1.next = ListNode(1)
list1.next.next = ListNode(13)
list1.next.next.next = ListNode(6)
list1.next.next.next.next = ListNode(9)
list1.next.next.next.next.next = ListNode(5)
s = Solution()

list2 = ListNode(1000000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)
print(s.mergeInBetween(list1, 3, 4, list2))