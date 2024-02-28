# Definition for a binary tree node.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#### MY ORIGINAL SOLN #########################################
# class Solution:
#     def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
#         queue = []
#         queue.append(root.val)

#         def helper(root):
#             res1 = res2 = None
#             if root.left:
#                 queue.append(root.left.val)
#                 res1 = helper(root.left)
#             if root.right:
#                 queue.append(root.right.val)
#                 res2 = helper(root.right)
#             if res1 and res2:
#                 res = max(res1, res2)
#             elif res1 and not res2:
#                 res = res1
#             elif res2 and not res1:
#                 res = res2
#             else:
#                 res = 0
            
#             popped = queue.pop()
#             for node in queue:
#                 res = max(res, abs(popped - node))
#             return res

#         return helper(root)
#############################################################################
        
##### BOTTOM UP APPROACH #######################################################
# class Solution:
#     def maxAncestorDiff(self, root):
#         m = [0]
#         self.dfs(root, m)
#         return m[0]

#     def dfs(self, root, m):
#         if not root:
#             return float('inf'), float('-inf')

#         left = self.dfs(root.left, m)
#         right = self.dfs(root.right, m)

#         min_val = min(root.val, min(left[0], right[0]))
#         max_val = max(root.val, max(left[1], right[1]))

#         m[0] = max(m[0], max(abs(min_val - root.val), abs(max_val - root.val)))

#         return min_val, max_val
################################################################################
    
##### TOP DOWN APPROACH ######################################################################

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min
            
            cur_min = min(node.val, cur_min)
            cur_max = max(node.val, cur_max)

            return max(dfs(node.left, cur_min, cur_max), dfs(node.right, cur_min, cur_max))
        
        return dfs(root, root.val, root.val)

###############################################################################################

s = Solution()
l = TreeNode(8)
l.left = TreeNode(3)
l.left.left = TreeNode(1)
l.left.right = TreeNode(6)
l.left.right.left = TreeNode(4)
l.left.right.right = TreeNode(7)
l.right = TreeNode(10)
l.right.right = TreeNode(14)
l.right.right.left = TreeNode(13)

print(s.maxAncestorDiff(l))

        




        