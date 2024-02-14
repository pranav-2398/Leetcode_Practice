# Definition for a binary tree node.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### MY SOLN #################################################################
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []

#         def dfs(root, n, rightBias):
#             if not root:
#                 return
            
#             if len(res) <= n:
#                 res.append([root.val])
#             else:
#                 if rightBias:
#                     res[n].append(root.val)
#                 else:
#                     res[n].insert(0, root.val)
            
#             dfs(root.left, n + 1, not rightBias)
#             dfs(root.right, n + 1, not rightBias)
            
        
#         dfs(root, 0, True)

#         return res
################################################################################
    
### QUEUE SOLN #################################################################
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        i = 0

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                if i % 2 == 0:
                    res.append(level)
                else:
                    res.append(list(reversed(level)))
            i += 1

        return res

##################################################################################  
s = Solution()
l = TreeNode(1)
l.left = TreeNode(2)
l.left.left = TreeNode(4)
l.right = TreeNode(3)
l.right.right = TreeNode(5)
print(s.zigzagLevelOrder(l))