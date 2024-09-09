from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## MY SOLN #################################################################################
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for i in range(m)]
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while head and top <= bottom and left <= right:
            for i in range(left, right + 1):
                if not head:
                    break
                matrix[top][i] = head.val
                head = head.next if head.next else None
            top += 1
            
            for j in range(top, bottom + 1):
                if not head:
                    break
                matrix[j][right] = head.val
                head = head.next if head.next else None
            right -= 1
            
            for i in range(right, left - 1, -1):
                if not head:
                    break
                matrix[bottom][i] = head.val
                head = head.next if head.next else None
            bottom -= 1

            for j in range(bottom, top - 1, -1):
                if not head:
                    break
                matrix[j][left] = head.val
                head = head.next if head.next else None
            left += 1
        
        return matrix
## LESS CODE SOLN ###########################################################################        
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for i in range(m)]
        top, bottom = 0, m - 1 
        left, right = 0, n - 1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c, d = 0, 0, 0 #current row, col & direction

        while head:
            dr, dc = directions[d]

            while (head and left <= c <= right and top <= r <= bottom and grid[r][c] == -1):
                grid[r][c] = head.val
                head = head.next
                r, c = r + dr, c + dc
        
            r, c = r - dr, c - dc
            d = (d + 1) % 4
            dr, dc = directions[d]
            r, c = r + dr, c + dc
        
        return grid
################################################################################################    
s = Solution()
head = ListNode(3)
head.next = ListNode(0)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next.next.next.next= ListNode(2)
head.next.next.next.next.next.next.next.next.next.next= ListNode(5)
head.next.next.next.next.next.next.next.next.next.next.next= ListNode(5)
head.next.next.next.next.next.next.next.next.next.next.next.next= ListNode(0)
print(s.spiralMatrix(3, 5, head))