# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

### MY SOLN ######################################################################################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(node):
            q = deque([])

            start = root
            while start:
                q.append(start)
                if node.val == start.val:
                    break
                elif node.val > start.val:
                    start = start.right
                else:
                    start = start.left
            
            return q
        
        p_queue = find(p)
        q_queue = find(q)

        prev = None
        while p_queue and q_queue:
            p_node, q_node = p_queue.popleft(), q_queue.popleft()

            if p_node == q_node:
                prev = p_node
        
        return prev
##################################################################################################
    
#### OPTIMISED SOLN ##############################################################################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

###################################################################################################