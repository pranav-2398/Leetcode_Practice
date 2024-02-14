# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### MY SOLN #########################################################
     
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []

#         def dfs(root, n):
#             if not root:
#                 return
            
#             if len(res) <= n:
#                 res.append([root.val])
#             else:
#                 res[n].append(root.val)
            
#             dfs(root.left, n + 1)
#             dfs(root.right, n + 1)
        
#         dfs(root, 0)

#         return res

#######################################################################
        
### USING QUEUES ######################################################
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res
    
##########################################################################