from collections import deque
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

##### MY SOLN #######################################################
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        queue = deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            level = []
            for _ in range(qlen):
                node = queue.popleft()
                if queue:
                    node.next = queue[0]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue.extend(level)

        return root

########################################################################
    
#### MY SOLN IMPROVED #########################################

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        queue = deque()
        queue.append(root)

        while queue:
            qlen = len(queue)

            for i in range(qlen):
                node = queue.popleft()
                if queue and i < qlen-1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

###########################################################################

### CONST SPACE SOLN ######################################################

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        
        return root

##############################################################################